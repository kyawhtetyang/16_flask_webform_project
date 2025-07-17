from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")

        if not name or not age:
            return render_template("result.html", message="Missing name or age.")

        return render_template("result.html", message=f"Hello {name}, you are {age} years old!")

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)