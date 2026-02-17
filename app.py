# flask - python web fw  - web apps , rest apis and microservices
from flask import Flask
from flask import Flask, jsonify, request

# creates a flask object
app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to Flask web server!"

# get method end point
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob" , "Charlie"]})

# post method end point
@app.route('/users', methods =['POST'])
def add_users():
    data = request.get_json()
    return jsonify(data),201

# put request
@app.route('/users/<int:id>', methods =['PUT'])
def update_users(id):
    return jsonify({"Message": f"user {id} is updated"})


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return jsonify({"message": f"User {id} deleted"})


@app.route('/users/<int:id>', methods=['PATCH'])
def patch_user(id):
    data = request.get_json()
    return jsonify({
        "message": "User updated partially",
        "user_id": id,
        "updated_fields": data
    })

#  run the below  code only if this file is executed directly and not when imported
if __name__ == "__main__":
    app.run(debug = True)
# run the local server - 127.0.0.1 or localhost:5000
# enable the debugging  mode


