from project import validate_time_format, view_alarms

TEST_FILE = "alarms.txt"


def setup_module(module):
    # Create a test file with some initial alarms
    with open(TEST_FILE, "w") as f:
        f.write("06:30\n14:45\n23:59\n")


# Tests
def test_validate_time_format_valid():
    assert validate_time_format("00:00")
    assert validate_time_format("23:59")
    assert validate_time_format("09:05")


def test_validate_time_format_invalid():
    assert not validate_time_format("9:05")
    assert not validate_time_format("24:00")
    assert not validate_time_format("12:60")
    assert not validate_time_format("xx:yy")
    assert not validate_time_format("1234")


def test_view_alarms_returns_lines():
    alarms = view_alarms()
    assert isinstance(alarms, list)
    assert len(alarms) == 3
    assert alarms[0].strip() == "06:30"
    assert alarms[2].strip() == "23:59"
