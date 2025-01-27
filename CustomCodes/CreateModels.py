def create_models(entities):
    result = ""
    for entity in entities:
        attributes = entities[entity]
        result += f"class {entity}(db.Model):\n"
        for attribute in attributes:
            type_ = attributes[attribute]
            result += f"\t{attribute} = db.Column(db.{type_}"
            if attribute == 'id':
                result += ", primary_key=True"
            result += ")\n"
        result += '\n'
    return result