from CustomCodes.CreateModels import create_models
from CustomCodes.Header import header
from CustomCodes.Create import create
from CustomCodes.Update import update
from CustomCodes.Delete import delete
from CustomCodes.List import list
from CustomCodes.Discount import discount

class StoreDSLCodeGenerator:
    def __init__(self):
        self.entities = {}  # To store defined entities and their attributes
        self.output = []  # To store generated code
        self.query_stack = []  # To handle traversal
        self.code_queries = []  # To store parsed queries from the traversal
        self.footer = []

    def parse_tree(self, traversal):
        attributes = {}

        for node in traversal:
            node = node['label']

            if node in {"attribute", "keyValuePair"}:
                value = self.query_stack.pop().replace("\"", "")
                key = self.query_stack.pop().replace("\"", "")
                attributes[key] = value

            elif node == "define":
                entity = self.query_stack.pop().replace("\"", "")
                self.entities[entity] = attributes
                attributes = {}

            elif node in {"create", "update", "delete", "discount"}:
                if node == "discount":
                    discount_value = int(self.query_stack.pop().replace("\"", ""))
                    attributes['discount'] = discount_value
                entity = self.query_stack.pop().replace("\"", "")
                self.code_queries.append([node, entity, attributes])
                attributes = {}

            else:
                self.query_stack.append(node)

        if len(self.query_stack):
            self.query_stack.pop()
        while self.query_stack:
            self.code_queries.append(['list', self.query_stack.pop().replace("\"", ""), {}])

    def generate_operation_code(self, operation, entity, data):
        operation_code = {
            "create": self.create,
            "update": self.update,
            "delete": self.delete,
            "discount": self.discount
        }.get(operation, lambda *_: f"""
\ttry:
\t\tentries = {entity.lower()}.query.all()
\t\tfor entry in entries:
\t\t\tprint(entry)
\texcept:
\t\tpass
""")
        return operation_code(entity, data)

    def create(self, entity, data):
        attributes = ",\n".join([f"\t\t\t{key} = '{value}'" for key, value in data.items() if key != 'id'])
        return f"""
\ttry:
\t\t{entity.lower()} = {entity}(
\t\t\tid = '{data['id']}',
{attributes}
\t\t)
\t\tdb.session.add({entity.lower()})
\t\tdb.session.commit()
\texcept:
\t\tpass
"""

    def delete(self, entity, data):
        return f"""
\ttry:
\t\t{entity.lower()} = {entity}.query.get('{data['id']}')
\t\tif {entity.lower()}:
\t\t\tdb.session.delete({entity.lower()})
\t\t\tdb.session.commit()
\texcept:
\t\tpass
"""

    def update(self, entity, data):
        updates = "\n".join([f"\t\t\t{entity.lower()}.{key} = '{value}'" for key, value in data.items() if key != 'id'])
        return f"""
\ttry:
\t\t{entity.lower()} = {entity}.query.get('{data['id']}')
\t\tif {entity.lower()}:
{updates}
\t\t\tdb.session.commit()
\texcept:
\t\tpass
"""

    def discount(self, entity, data):
        return f"""
\ttry:
\t\t{entity.lower()} = {entity}.query.get('{data['id']}')
\t\tif {entity.lower()}:
\t\t\t{entity.lower()}.price -= {entity.lower()}.price * (100 - float({data['discount']})) / 100
\t\t\tdb.session.commit()
\texcept:
\t\tpass
"""

    def generate_code(self, traversal):
        self.parse_tree(traversal)

        self.output.append(header())
        self.output.append(create_models(self.entities))

        operations = ["""
# Create the database
with app.app_context():
\tdb.create_all()
"""]

        for entity in self.entities:
            queries = {
                "create": create,
                "delete": delete,
                "update": update,
                "list": list
            }
            for query_name, query_function in queries.items():
                self.footer.append(query_function(entity, self.entities))

        for query, entity, data in self.code_queries:
            operations.append(self.generate_operation_code(query, entity, data))

        self.output.extend(operations)
        self.footer.append("""
if __name__ == '__main__':
\tapp.run(debug=True)""")
        self.output.extend(self.footer)
        return '\n'.join(self.output)