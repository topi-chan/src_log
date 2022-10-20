import pandas
import pytest
import pandas as pd
from .data_io import read_table, PD_COLUMN_NAMES
from .operations import mf_ip


def test_read_data():
    test_df = read_table("log_test.txt")

    assert type(test_df) == pd.DataFrame  # test type
    assert len(test_df) == 10  # test row len
    assert len(test_df.columns) == 10  # test col len
    assert list(test_df.columns) == PD_COLUMN_NAMES  # test exact names


class TestEnv:
    """Create environment to use in tests"""

    def __init__(self):
        self.test_df = read_table("log_test.txt")
        self.analyze_result = {"Events per second": "5.476362402868889"}



def test_operations():
    pass
