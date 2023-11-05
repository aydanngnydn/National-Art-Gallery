from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run("0.0.0.0", port = port)