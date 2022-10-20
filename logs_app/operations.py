import pandas as pd


# Return most used IP address by using pandas mode(), then selecting element [0], which is the address
def mf_ip(ip_df: pd.DataFrame) -> str:
    series_mf = ip_df["Client IP address"].mode()
    return series_mf[0]


# Return least used IP address by pandas idxmin() method
def lf_ip(ip_df: pd.DataFrame) -> str:
    return ip_df["Client IP address"].value_counts().idxmin()


# Return events per seconds
def e_ps(e_df: pd.DataFrame) -> float:
    min_unix_time_value = e_df["Timestamp in seconds since the epoch"].value_counts().idxmin()  # Return first event
    max_unix_time_value = e_df["Timestamp in seconds since the epoch"].mode()[0]  # Return last event
    event_time = max_unix_time_value - min_unix_time_value  # Return time value in seconds.milliseconds between them
    number_of_events = len(e_df.index)  # Return total number of events
    result = number_of_events / event_time  # Return how many events per seconds
    return result


# Return total bytes by summing the colum with pandas
def bytes_total(bytes_df: pd.DataFrame) -> int:
    return bytes_df["Response size in bytes"].sum()
