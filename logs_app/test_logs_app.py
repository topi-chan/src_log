import numpy
import pandas as pd
import pytest

from logs_app.data_io import PD_COLUMN_NAMES, load_input_data, read_table, save_results
from logs_app.operations import bytes_total, e_ps, lf_ip, mf_ip

from .main import base_task


def test_read_data():
    test_df = read_table("log_test.txt")

    assert type(test_df) == pd.DataFrame  # test type
    assert len(test_df) == 100  # test row len
    assert len(test_df.columns) == 10  # test col len
    assert list(test_df.columns) == PD_COLUMN_NAMES  # test exact names


test_df = read_table("log_test.txt")


def test_compare_ips():
    lf_value = lf_ip(test_df)
    mf_value = mf_ip(test_df)

    assert type(lf_value) is str and type(mf_value) is str
    assert mf_value != lf_value


def test_eps():
    eps_result = e_ps(test_df)

    assert test_df["date"] is not None
    assert type(test_df["date"]) is pd.core.series.Series
    assert eps_result is not None and type(eps_result) is float


def test_bytes_total():
    bytes_result = bytes_total(test_df)

    assert bytes_result is not None
    assert type(bytes_result) is numpy.int64


def test_load_input_data_simple_txt_file():
    text_input_result = load_input_data("log_test.txt")
    assert type(text_input_result) is pd.DataFrame
    assert len(text_input_result) == 100
    assert len(text_input_result.columns) == 10
    assert list(text_input_result.columns) == PD_COLUMN_NAMES


def test_load_input_data_last_condition():
    with pytest.raises(TypeError):
        text_input_result = load_input_data("/wrong_path")
        assert text_input_result is None


def test_save_results():
    json_result = save_results("Test Col", "str", "path")
    assert json_result is None


def test_save_results_flt():
    json_result = save_results("Test Col", 345.2, "path")
    assert json_result is None


def test_save_results_int():
    json_result = save_results("Test Col", 345, "path")
    assert json_result is None


def test_base_task():
    base_task_df = base_task("log_test.txt")
    assert base_task_df is not None
