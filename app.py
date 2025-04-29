from flask import Flask, jsonify, request
from users import add_user, get_users, delete_user

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    user = add_user(data['name'])
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def list_users():
    return jsonify(get_users())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    success = delete_user(user_id)
    if success:
        return jsonify({'message': f'User {user_id} deleted'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
