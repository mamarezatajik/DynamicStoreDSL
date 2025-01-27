def discount(entity, entities):
    return f"""
# Apply Discount to {entity}
@app.route('/applyDiscount', methods=['POST'])
def apply_discount():
\tdata = request.get_json()
\t{entity.lower()} = {entity}.query.get(data['id'])
\tif {entity.lower()}:
\t\t{entity.lower()}.price -= {entity.lower()}.price * (data['discount'] / 100.0)
\t\tdb.session.commit()
\t\treturn jsonify({{"message": "Discount applied successfully"}}), 200
\telse:
\t\treturn jsonify({{"error": "{entity} not found"}}), 404
"""