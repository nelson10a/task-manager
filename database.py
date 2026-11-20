import psycopg


def connect_db():
    return psycopg.connect(
        "dbname=task_manager_db user=owl"
    )


def get_manufacturers():
    connection = connect_db()

    with connection.cursor() as cursor:
        cursor.execute("select * from manufacturer;")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    connection.close()
    return rows

def get_parts_for_manufacturer(manufacturer_name):
    connection = connect_db()

    with connection.cursor() as cursor:
        cursor.execute("""SELECT parts.name FROM parts JOIN vehicle ON parts.vehicle_id = vehicle.vehicle_id JOIN manufacturer ON vehicle.manufacturer_id = manufacturer.manufacturer_id WHERE manufacturer.name = %s; """, (manufacturer_name,))
        rows = cursor.fetchall()

    connection.close()
    return [row[0] for row in rows]



def add_manufacturer(name):
    connection = connect_db()

    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO manufacturer (name)
                       VALUES (%s) RETURNING manufacturer_id, name;""", (name,)) 
        row = cursor.fetchone()
        connection.commit() 
       
    connection.close()
    return row
        







if __name__ == "__main__":
    manufacturers = get_manufacturers()

    parts_for_manufacturer = get_parts_for_manufacturer()