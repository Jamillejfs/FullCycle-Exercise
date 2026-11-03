from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "API principal  atualizada!"


@app.route("/version")
def version():
    return {"version": "1.1.0"}


if __name__ == "__main__":
    app.run(debug=True)
