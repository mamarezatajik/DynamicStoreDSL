def list(entity, entities):
    attributes = entities[entity]
    return f"""
# List {entity}s
@app.route('/list{entity}s', methods=['GET'])
def list_{entity.lower()}s():
\t{entity.lower()}s = {entity}.query.all()
\t{entity.lower()}_list = [{{
\t\t{',\n\t\t'.join([f'"{attr}": {entity.lower()}.{attr}' for attr in attributes])}
\t}} for {entity.lower()} in {entity.lower()}s]
\treturn jsonify({entity.lower()}_list), 200
"""