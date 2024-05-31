import pytest
from dundie.database import connect, commit, add_person
from dundie.core import add


@pytest.mark.unit
def test_add_movement():
    db = connect()

    pk = "jim@doe.com"
    data = {"role": "Salesman", "dept": "Management", "name": "Jim Doe"}
    _, created = add_person(db, pk, data)
    assert created is True

    pk = "joe@doe.com"
    data = {"role": "Manager", "dept": "Sales", "name": "Joe Doe"}
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    add(-30, email="jim@doe.com")

    db = connect()
    assert db["balance"]["jim@doe.com"] == 470
