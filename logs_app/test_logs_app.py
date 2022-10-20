import pandas as pd
from logs_app.data_io import read_table, PD_COLUMN_NAMES
from logs_app.operations import mf_ip, lf_ip, e_ps, bytes_total
from .main import mfip, base_task
import numpy


def test_read_data():
    test_df = read_table("log_test.txt")

    assert type(test_df) == pd.DataFrame  # test type
    assert len(test_df) == 100  # test row len
    assert len(test_df.columns) == 10  # test col len
    assert list(test_df.columns) == PD_COLUMN_NAMES  # test exact names


class TestEnv:
    """Create environment to use in tests"""

    def __init__(self):
        self.test_df = read_table("log_test.txt")
        self.analyze_result_eps = {"Events per second": "5.476362402868889"}


env = TestEnv()


def test_compare_ips():
    lf_value = lf_ip(env.test_df)
    mf_value = mf_ip(env.test_df)

    assert type(lf_value) is str and type(mf_value) is str
    assert mf_value != lf_value


def test_eps():
    eps_result = e_ps(env.test_df)

    assert env.test_df['date'] is not None
    assert type(env.test_df['date']) is pd.core.series.Series
    assert eps_result is not None and type(eps_result) is float


def test_bytes_total():
    bytes_result = bytes_total(env.test_df)

    assert bytes_result is not None
    assert type(bytes_result) is numpy.int64


def test_base_task():
    base_task_df = base_task("log_test.txt")
    assert base_task_df is not None
