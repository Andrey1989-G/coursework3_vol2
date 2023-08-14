from utils import utils_for_file

def test_utils_for_file():
    assert type(utils_for_file.load_data()) == list