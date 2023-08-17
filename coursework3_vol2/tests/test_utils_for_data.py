from utils.utils_for_data import slice_data, magic_with_N_card, magic_with_date
from utils.utils_for_file import load_data
def test_utils_for_file():
    assert type(slice_data(load_data())) == list
    assert len(magic_with_N_card()) == 24
    assert type(magic_with_N_card()) == str
    assert len(magic_with_date()) == 10
    assert type(magic_with_date()) == str