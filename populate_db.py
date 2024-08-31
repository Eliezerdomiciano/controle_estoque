import random  # Importa o módulo random
from app import app  # Importa o app Flask para garantir o contexto
from extensions import db
from app import Cable, GBIC


def generate_serial_numbers(existing_serials, count):
    serials = set()
    while len(serials) < count:
        serial = f"SN{random.randint(100000, 999999)}"
        if serial not in existing_serials:
            serials.add(serial)
    return list(serials)


def generate_part_number(manufacturer):
    prefixes = {"Cisco": "FSF", "Juniper": "GRF", "Huawei": "TRT", "Datacom": "DDT"}
    suffix = random.choice(["50M", "30M", "20M", "10M"])
    return f"{prefixes[manufacturer]}-{suffix}"


def populate_db():
    manufacturers = ["Cisco", "Juniper", "Huawei", "Datacom"]
    positions_gbic = {
        "Cisco": "RACK_ARF3",
        "Huawei": "RACK_ARF2",
        "Juniper": "RACK_ARF1",
        "Datacom": "RACK_ARF4",
    }
    positions_cable = ["Rack 1", "Rack 2", "Rack 3", "Rack 4", "Rack 5"]

    existing_serials = set()

    # Generate unique serial numbers
    serials_gbic = generate_serial_numbers(existing_serials, 500)
    existing_serials.update(serials_gbic)
    serials_cable = generate_serial_numbers(existing_serials, 500)

    # Populating the GBIC table
    gbics = []
    for i in range(500):
        manufacturer = random.choice(manufacturers)
        gbics.append(
            GBIC(
                serial_number=serials_gbic[i],
                part_number=generate_part_number(manufacturer),
                model=f"Model {random.choice(['X', 'Y', 'Z'])}",
                manufacturer=manufacturer,
                position=positions_gbic[manufacturer],
                status=random.choice(["In Use", "In Stock"]),
            )
        )

    # Populating the Cable table
    cables = []
    for i in range(500):
        manufacturer = random.choice(manufacturers)
        cables.append(
            Cable(
                serial_number=serials_cable[i],
                part_number=generate_part_number(manufacturer),
                position=random.choice(positions_cable),
                cable_type=random.choice(["Fiber", "Copper"]),
            )
        )

    db.session.bulk_save_objects(gbics)
    db.session.bulk_save_objects(cables)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():  # Garante que o contexto da aplicação está ativo
        db.create_all()
        populate_db()
