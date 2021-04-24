from flask import Flask
from flask import request

app = Flask(__name__)
first_to_last_names = {"anna": "last_name1", "mike": "last_name2"}


@app.route('/hello')
def hello_world():
    return 'Hello, '


@app.route('/user/<first_name>')
def show_user_profile(first_name: str):
    return look_up_user_info(first_name)


@app.route('/login', methods=['POST'])
def login():
    name = request.json
    return look_up_user_info(name['first_name'], name['last_name'])


def look_up_user_info(first_name: str, last_name: str = None):
    if first_name in first_to_last_names:
        return "User is: " + first_to_last_names[first_name]
    else:
        if last_name is not None:
            first_to_last_names[first_name] = last_name
        return "User Updated!"


if __name__ == "__main__":
    app.run()
