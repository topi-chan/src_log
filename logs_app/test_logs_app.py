import pandas
import pytest
import pandas as pd
from .data_io import read_table, PD_COLUMN_NAMES, save_results
from .operations import mf_ip, lf_ip, e_ps, bytes_total
#from .main import base_task


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
        self.analyze_result_eps = {"Events per second": "5.476362402868889"}


env = TestEnv()


# def test_base_task():
#     base_task_df = base_task()
#     assert base_task_df == env.test_df

def test_compare_ips():
    lf_value = lf_ip(env.test_df)
    mf_value = mf_ip(env.test_df)

    assert mf_value != lf_value

