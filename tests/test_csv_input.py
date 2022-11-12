import pytest
import sys
# set path
sys.path.append('../')
from app.main import load_csv


@pytest.fixture
def example_load_data():
    return [['Movie Name', 'Release Year', 'Rating', 'id'],
            ['Cars', '2006', '7.2', '11'],
            ['The Darjeeling Limited', '2007', '7.2', '13'],
            ['Marley & Me', '2008', '7.0', '15'],
            ['The Internship', '2013', '6.3', '22']]

# Test load_csv returns a list type
def test_load_csv_return():
    assert type(load_csv('test_files/test_input_happy.csv')) == list

# Test load_csv output data
def test_load_csv_input(example_load_data):
    filename = 'test_files/test_input_happy.csv'
    assert load_csv(filename) == example_load_data

# assert mismatched headers raises ValueError
def test_load_csv_header_names():
    with pytest.raises(ValueError, match="Mismatching headers, exiting."):
        load_csv('test_files/test_input_different_cols.csv')

# assert mismatched row length raises ValueError
def test_load_csv_row_length():
    with pytest.raises(ValueError, match="Mismatching row length, exiting."):
        load_csv('test_files/test_input_extra_cols.csv')
