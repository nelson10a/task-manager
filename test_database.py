from database import get_manufacturers, get_parts_for_manufacturer



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