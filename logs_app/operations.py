import pandas as pd


# Return most used IP address by using pandas mode(), then selecting element [0], which is the address
def mf_ip(ip_df: pd.DataFrame) -> str:
    series_mf = ip_df["Client IP address"].mode()
    return series_mf[0]


# Return least used IP address by pandas idxmin() method
def lf_ip(ip_df: pd.DataFrame) -> str:
    return ip_df["Client IP address"].value_counts().idxmin()


# Return mean timestamp TODO: check
def e_ps(e_df: pd.DataFrame) -> float:
    return e_df["Timestamp in seconds since the epoch"].mean()


# Return total bytes by summing the colum with pandas
def bytes_total(bytes_df: pd.DataFrame) -> int:
    return bytes_df["Response size in bytes"].sum()
