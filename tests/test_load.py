import pytest
from dundie.core import load
from .constants import PEOPLE_FILE
from dundie.database import EMPTY_DB, connect


# @pytest.mark.unit
# @pytest.mark.high
# def test_load_positive_has_len_2():
#     """Test load function."""
#     assert len(load(PEOPLE_FILE)) == 2


# @pytest.mark.unit
# @pytest.mark.high
# def test_load_positive_stats_with_j():
#     """Test load function."""
#     assert load(PEOPLE_FILE)[0]["name"] == "Jim Halpert"


# @pytest.mark.unit
# def test_db_schema():
#     load(PEOPLE_FILE)
#     db = connect()
#     assert db.keys() == EMPTY_DB.keys()
