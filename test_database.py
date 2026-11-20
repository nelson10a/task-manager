from database import get_manufacturers, get_parts_for_manufacturer, add_manufacturer, connect_db
import pytest


"""fixture starts
   ↓
delete old Volkswagen if present
   ↓
yield
   ↓
run the test
   ↓
delete Volkswagen again
   ↓
test leaves database clean"""

@pytest.fixture
def clean_volkswagen():
    connection = connect_db()

    with connection.cursor() as cursor:
        cursor.execute("delete from manufacturer where name = %s;", ("Vokswagen",))

        connection.commit()

    connection.close

    yield

    connection = connect_db()

    with connection.cursor() as cursor:
        cursor.execute("delete from manufacturer where name = %s;", ("Volkswagen",))
        connection.commit()
    
    connection.close()


def test_get_manufacturers():
    result = get_manufacturers()

    assert (1, "Toyota") in result
    assert (2, "Honda") in result
    assert (3, "Mercedes") in result

def test_get_parts_for_manufacturer():
    result = get_parts_for_manufacturer("Toyota")

    assert "Gearbox" in result
    assert "Alternator" in result
    assert "Starter Motor" in result




def test_add_manufacturer(clean_volkswagen):
    result = add_manufacturer("Volkswagen")

    assert result[1] == "Volkswagen"