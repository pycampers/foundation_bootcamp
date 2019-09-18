from flask import Flask, request
from tinydb import TinyDB, Query

# Here we are making a db object, query object and app object.
db = TinyDB('user_db.json')
User = Query()
app = Flask(__name__)


def verify_username_password_tinydb(username, password_from_user):
    user_details = db.search(User.username == username)

    if username == user_details[0]["username"]:
        correct_password = user_details[0]["password"]
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
    message = verify_username_password_tinydb(username, password_from_user)
    return message


@app.route("/signup")
def signup():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == None or password == None:
        return "Please enter username and password."
    else:
        db.insert({"username":username, "password":password})
        return f"User {username} signed up."

@app.route("/change_password")
def change_password():
    username = request.args.get("username")
    old_password = request.args.get("old_password")
    new_password = request.args.get("new_password")
  
    if username == None or old_password == None or new_password == None:
        return "Please enter username, old password and new password."
    else:
        message = verify_username_password_tinydb(username, old_password)
        if message == "password is correct.":
            # users_dict[username]["password"] = new_password
            db.update({"password":new_password}, User.username == username)

            return "Password have been updated."
        else:
            return message


if __name__ == "__main__":
    app.run(debug=True)