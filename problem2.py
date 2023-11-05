from flask import Flask, request, jsonify

app= Flask(__name__)

userData={}

@app.route('/')
def index():
    return 'Welcome to your dictionary app!'


@app.route('/create', methods=['POST'])
def add_user():
    data = request.get_json()
    username=data.get('username')
    if username:
        userData[username]=data
        return jsonify({'message': 'User added successfully'},userData)
    else:
        return jsonify({'message':"Username is required"}), 400


@app.route('/read',methods=['GET'])
def get_user():
    return jsonify(userData)
    
@app.route('/update/<username>',methods=['PUT'])
def update_user(username):
    data=request.get_json()
    if username in userData:
        userData[username]=data
        return jsonify({'message': 'User updated successfully'},userData)
    else:
        return jsonify({'message': 'User not found'}), 400

@app.route('/delete/<username>', methods=['DELETE'])
def delete_user(username):
    if username in userData:
        del userData[username]
        return jsonify({'message':'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 400
    

if __name__ == '__main__':
    app.run(debug=True)