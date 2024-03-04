<<<<<<< HEAD
# app.py

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

organizations = ["Organization 1", "Organization 2", "Organization 3", "Organization 4", "Organization 5"]
registered_users = {}

@app.route('/')
def home():
    return render_template('home.html', organizations=organizations)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    organization = request.form.get('organization')

    if not name or not organization or organization not in organizations:
        return redirect('/')

    registered_users[name] = organization
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('users.html', users=registered_users)

if __name__ == '__main__':
=======
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analyze", methods=["GET"])
def analyze():
    try:
        number = int(request.args.get("number"))
        result = "Even" if number % 2 == 0 else "Odd"
    except (ValueError, TypeError):
        result = "Not an integer"

    return render_template("result.html", result=result)

@app.route("/error")
def error():
    return "Error: Please provide a valid query parameter."

if __name__ == "__main__":
>>>>>>> origin/main
    app.run(debug=True)
