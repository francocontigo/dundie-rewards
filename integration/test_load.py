import pytest
from subprocess import check_output, CalledProcessError


@pytest.mark.integration
@pytest.mark.medium
def test_load_postive_call_load_command():
    """Test command load"""
    out = (
        check_output(["dundie", "load", "tests/assets/people.csv"])
        .decode("utf-8")
        .split("\n")
    )
    assert len(out) == 2


@pytest.mark.integration
@pytest.mark.medium
def test_load_negative_call_load_command_with_wrong_params():
    """Test command load"""
    with pytest.raises(CalledProcessError) as error:
        check_output(["dundie", "loady", "tests/assets/people.csv"]).decode(
            "utf-8"
        ).split("\n")
    assert "status 2" in str(error.getrepr())
