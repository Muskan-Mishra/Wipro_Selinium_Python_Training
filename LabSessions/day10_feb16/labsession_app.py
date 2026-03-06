from flask import Flask, request, jsonify

app = Flask(__name__)

customers = {}
current_id = 1

@app.route("/customers", methods=["POST"])
def create_customer():
    global current_id
    data = request.json
    data["id"] = current_id
    customers[current_id] = data
    current_id += 1
    return jsonify(data), 201

@app.route("/customers/<int:id>", methods=["GET"])
def get_customer(id):
    if id in customers:
        return jsonify(customers[id]), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/customers/<int:id>", methods=["PUT"])
def update_customer(id):
    if id in customers:
        data = request.json
        data["id"] = id
        customers[id] = data
        return jsonify(data), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/customers/<int:id>", methods=["PATCH"])
def patch_customer(id):
    if id in customers:
        data = request.json
        customers[id].update(data)
        return jsonify(customers[id]), 200
    return jsonify({"error": "Not found"}), 404


@app.route("/customers/<int:id>", methods=["DELETE"])
def delete_customer(id):
    if id in customers:
        del customers[id]
        return "", 204
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)