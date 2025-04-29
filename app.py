from flask import Flask, jsonify, request
from users import add_user, get_users

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

if __name__ == '__main__':
    app.run(debug=True)
