from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get("name")
    result = f'Hello {name}, How are you today?'
    return result

@app.route('/add')
def addition():
    # http://127.0.0.1:5000/add?first_no=3&second_no=5
    first_no = request.args.get('first_no')
    second_no = request.args.get('second_no')
    if first_no != None and second_no != None:
        addition_output = int(first_no) + int(second_no)
        response = f"The sum of these two numbers in {addition_output}"
    else:
        response = "Please pass two number in url."

    return response


if __name__ == "__main__":
    app.run(debug=True)