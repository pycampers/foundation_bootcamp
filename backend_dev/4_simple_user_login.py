from flask import Flask, request

app = Flask(__name__)

users_dict = {"hasan":{"username":"hasan", "password":"1234"},
              "sri":  {"username":"sri", "password":"4321"}}


def verify_username_password(username, password_from_user):
    if username in users_dict.keys():
        correct_password = users_dict[username]["password"]
        if correct_password == password_from_user:
            message = "password is correct."
            return message
        else:
            message = "incorrect password"
            return message
    else:
        message = "user doesn't exists."
        return message

@app.route('/')
def home():
    message = """
    <html>
        <body>
            <p> Go to <a href='/login'>/login</a></p>
            <p> Go to <a href='/signup'>/signup</a></p>
            <p> Go to <a href='/change_password'>/change_password</a></p>
        </body>
    </html>
    """
    return message

@app.route('/login')
def login():
    username = request.args.get("username")
    password_from_user = request.args.get("password")
    message = verify_username_password(username, password_from_user)
    return message

@app.route("/signup")
def signup():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == None or password == None:
        return "Please enter username and password."
    else:
        users_dict[username] = {"username":username, "password":password}
        print(users_dict.keys())
        return f"User {username} signed up."

@app.route("/change_password")
def change_password():
    username = request.args.get("username")
    old_password = request.args.get("old_password")
    new_password = request.args.get("new_password")

    message = verify_username_password(username, old_password)
    if message == "password is correct.":
        users_dict[username]["password"] = new_password
        return "Password have been updated."
    else:
        return message


if __name__ == "__main__":
    app.run(debug=True)