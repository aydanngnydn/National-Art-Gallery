from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run("0.0.0.0", port = port)