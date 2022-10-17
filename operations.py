import pandas as pd


def mf_ip(ip_df: pd.DataFrame) -> str:
    series_mf = ip_df["Client IP address"].mode()
    return series_mf[0]


def lf_ip(ip_df: pd.DataFrame) -> str:
    return ip_df["Client IP address"].value_counts().idxmin()


def e_ps(e_df: pd.DataFrame) -> float:
    return e_df["Timestamp in seconds since the epoch"].mean()


def bytes_total(bytes_df: pd.DataFrame) -> int:
    return bytes_df["Response size in bytes"].sum()
