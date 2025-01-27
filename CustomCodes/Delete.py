def delete(entity, entities):
    return f"""
# Delete {entity}
@app.route('/delete{entity}', methods=['POST'])
def delete_{entity.lower()}():
\tdata = request.get_json()
\t{entity.lower()} = {entity}.query.get(data['id'])
\tif {entity.lower()}:
\t\tdb.session.delete({entity.lower()})
\t\tdb.session.commit()
\t\treturn jsonify({{"message": "{entity} deleted successfully"}}), 200
\telse:
\t\treturn jsonify({{"error": "{entity} not found"}}), 404
"""