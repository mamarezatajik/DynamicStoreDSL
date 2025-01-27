def update(entity, entities):
    result = f"""
# Update {entity}
@app.route('/update{entity}', methods=['POST'])
def update_{entity.lower()}():
\tdata = request.get_json()
\t{entity.lower()} = {entity}.query.get(data['id'])
\tif {entity.lower()}:\n"""
    for attr in entities[entity]:
        if attr != 'id':
            result += f"\t\t{entity.lower()}.{attr} = data.get('{attr}', {entity.lower()}.{attr})\n"
    result += f"""\t\tdb.session.commit()
\t\treturn jsonify({{"message": "{entity} updated successfully"}}), 200
\telse:
\t\treturn jsonify({{"error": "{entity} not found"}}), 404
"""
    return result