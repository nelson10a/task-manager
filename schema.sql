CREATE TABLE manufacturer (
    manufacturer_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    name VARCHAR NOT NULL UNIQUE
);


CREATE TABLE vehicle (
    vehicle_id INTEGER PRIMARY KEY,
    manufacturer_id INTEGER NOT NULL,
    model VARCHAR NOT NULL,
    year INTEGER NOT NULL,

    FOREIGN KEY (manufacturer_id)
        REFERENCES manufacturer(manufacturer_id),

    UNIQUE (manufacturer_id, model, year),

    CHECK (year >= 1900)
);


CREATE TABLE parts (
    part_id INTEGER PRIMARY KEY,
    vehicle_id INTEGER NOT NULL,
    name VARCHAR NOT NULL,
    condition VARCHAR NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 0,
    price NUMERIC(10, 2) NOT NULL,

    FOREIGN KEY (vehicle_id)
        REFERENCES vehicle(vehicle_id),

    UNIQUE (vehicle_id, name),

    CHECK (quantity >= 0),
    CHECK (price >= 0)
);