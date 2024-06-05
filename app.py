from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cabeamento")
def cable():
    return render_template("cabeamento.html")


@app.route("/controle_peca")
def controle_peca():
    return render_template("controle_peca.html")


if __name__ == "__main__":
    app.run(debug=True)
