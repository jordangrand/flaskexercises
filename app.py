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
    app.run(debug=True)
