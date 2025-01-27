def create(entity, entities):
    result = f"""
# Create {entity}
@app.route('/create{entity}', methods=['POST'])
def create_{entity.lower()}():
\tdata = request.get_json()
\t{entity.lower()} = {entity}(\n"""
    for attr in entities[entity]:
        result += f"\t\t{attr}=data['{attr}'],\n"
    result += f"""\t\t)
\tdb.session.add({entity.lower()})
\tdb.session.commit()
\treturn jsonify({{"message": "{entity} created successfully"}}), 201
"""

    return result