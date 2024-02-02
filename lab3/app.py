
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)


def store_user_details(user_data):
    with open('users.txt', 'a') as file:
        json.dump(user_data, file)
        file.write('\n')


def get_user_details(user_id, mask_password=True):
    with open('users.txt', 'r') as file:
        for line in file:
            user_data = json.loads(line)
            if user_data['id'] == user_id:
                
                if mask_password:
                    user_data = {key: value if key != 'password' else '*' * len(value) for key, value in user_data.items()}
                return user_data
    return None


@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_data = {
            'id': 1 if not os.path.exists('users.txt') else len(open('users.txt').readlines()) + 1,
            'username': request.form['username'],
            'email': request.form['email'],
            'password': request.form['pwd'],  
        }
        store_user_details(user_data)
        return redirect(url_for('success'))
    return render_template('registration.html')


@app.route('/success')
def success():
    return 'Registration successful!'

@app.route('/user/<int:user_id>')
def view_user_details(user_id):
    user_data = get_user_details(user_id, mask_password=True)
    if user_data:
        return jsonify(user_data)
    else:
        return 'User not found.'

if __name__ == '__main__':
    app.run(debug=True)
