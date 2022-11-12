import sys
import pytest
# set path
sys.path.append('../')
from app.main import write_csv



@pytest.fixture
def example_write_data():
    return [['Name', 'Occupation', 'Salary'],
            ['Carlos', 'Welder', '75000'],
            ['Joe', 'Waiter', '60000']]


# Test load_csv output data by writing a test file
def test_check_write_output(example_write_data):
    filename = 'test_files/test_output.csv'
    write_csv(filename, example_write_data)
    with open(filename) as f:
        contents = f.read()
    assert contents == "Name,Occupation,Salary\nCarlos,Welder,75000\nJoe,Waiter,60000\n"
