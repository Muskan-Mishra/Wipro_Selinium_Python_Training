from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)
appointments = {}
appointment_counter = 1

VALID_TOKEN = "mysecrettoken123"



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"message": "Token missing"}), 401

        token = auth_header.split(" ")[1]

        if token != VALID_TOKEN:
            return jsonify({"message": "Invalid token"}), 403

        return f(*args, **kwargs)

    return decorated


# POST
@app.route("/v1/appointments", methods=["POST"])
@token_required
def create_appointment():
    global appointment_counter
    data = request.json

    data["appointmentId"] = appointment_counter
    appointments[appointment_counter] = data
    appointment_counter += 1

    return jsonify(data), 201


# GET
@app.route("/v1/appointments/<int:id>", methods=["GET"])
@token_required
def get_appointment(id):
    if id not in appointments:
        return jsonify({"message": "Appointment not found"}), 404

    return jsonify(appointments[id]), 200


# PUT
@app.route("/v1/appointments/<int:id>", methods=["PUT"])
@token_required
def update_appointment(id):
    if id not in appointments:
        return jsonify({"message": "Appointment not found"}), 404

    data = request.json
    data["appointmentId"] = id
    appointments[id] = data

    return jsonify(data), 200


# PATCH
@app.route("/v1/appointments/<int:id>", methods=["PATCH"])
@token_required
def patch_appointment(id):
    if id not in appointments:
        return jsonify({"message": "Appointment not found"}), 404

    data = request.json
    appointments[id].update(data)

    return jsonify(appointments[id]), 200


# DELETE
@app.route("/v1/appointments/<int:id>", methods=["DELETE"])
@token_required
def delete_appointment(id):
    if id not in appointments:
        return jsonify({"message": "Appointment not found"}), 404

    del appointments[id]
    return jsonify({"message": "Appointment deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)