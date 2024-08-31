from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from extensions import db  # Certifique-se de que está importando do extensions.py

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///network_inventory.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "your_secret_key"

db.init_app(app)


# Classes Cable e GBIC devem estar após a inicialização do db
class Cable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    part_number = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    cable_type = db.Column(db.String(100), nullable=False)


class GBIC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(100), nullable=False)
    part_number = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cabeamento", methods=["GET", "POST"])
def cable():
    if request.method == "POST":
        serial_number = request.form["serial_number"]
        part_number = request.form["part_number"]
        position = request.form["position"]
        cable_type = request.form["cable_type"]

        new_cable = Cable(
            serial_number=serial_number,
            part_number=part_number,
            position=position,
            cable_type=cable_type,
        )

        db.session.add(new_cable)
        db.session.commit()

        return redirect(url_for("cable"))

    cables = Cable.query.all()
    return render_template("cabeamento.html", cables=cables)


@app.route("/controle_peca", methods=["GET", "POST"])
def controle_peca():
    if request.method == "POST":
        serial_number = request.form["serial_number"]
        part_number = request.form["part_number"]
        model = request.form["model"]
        manufacturer = request.form["manufacturer"]
        position = request.form["position"]
        status = request.form["status"]

        new_gbic = GBIC(
            serial_number=serial_number,
            part_number=part_number,
            model=model,
            manufacturer=manufacturer,
            position=position,
            status=status,
        )

        db.session.add(new_gbic)
        db.session.commit()

        return redirect(url_for("controle_peca"))

    gbics = GBIC.query.all()
    return render_template("controle_peca.html", gbics=gbics)


@app.route("/update", methods=["POST"])
def update():
    data = request.form
    row_id = data.get("id")
    table = data.get("table")
    column = data.get("column")
    new_value = data.get("value")

    # Adiciona print statements para depuração
    print(f"Updating {table}: id={row_id}, column={column}, value={new_value}")

    if table == "Cable":
        item = Cable.query.get(row_id)
    elif table == "GBIC":
        item = GBIC.query.get(row_id)
    else:
        return jsonify({"message": "Invalid table"}), 400

    if not item:
        return jsonify({"message": "Item not found"}), 404

    setattr(item, column, new_value)
    db.session.commit()

    return jsonify({"message": "Value updated successfully"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
