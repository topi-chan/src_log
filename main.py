import pandas as pd

from json import dump


# Input

def take_input_data(path: str) -> pd.DataFrame:

    file = pd.read_csv(
        path,
        on_bad_lines="skip",
        sep=" ",
        skipinitialspace=True,
        names=[
            "Timestamp in seconds since the epoch",
            "Response header size in bytes",
            "Client IP address",
            "HTTP response code",
            "Response size in bytes",
            "HTTP request method",
            "URL",
            "Username",
            "Type of access/destination IP address",
            "Response type",
        ],
    )
    df = pd.DataFrame(data=file)
    return df


df = take_input_data("access.log")
print(df.head(n=1000))
print(df.columns[1:4])


# Operations
def mf_ip(ip_df_col: pd.DataFrame) -> str:
    return ip_df_col.mode()[0]


def lf_ip(ip_df_col: pd.DataFrame) -> str:
    return ip_df_col.value_counts().idxmin()


# 'since the epoch' - ale względem czasu pobrania, generowania logów? a jaki on był? średnio 2011 epochconverter.com
def e_ps(e_df_col: pd.DataFrame) -> float:
    return e_df_col.mean()


def bytes_total(bytes_df_col: pd.DataFrame) -> int:
    return bytes_df_col.sum()


# Output
def save_results(col_name: str, result: str | int | float, path: str = "result.json"):
    json_dict = {f"{col_name}": f"{result}"}
    with open(path, "w") as fp:
        dump(json_dict, fp, indent=4)


print(mf_ip(df["Client IP address"]))
print(lf_ip(df["Client IP address"]))
print(e_ps(df["Timestamp in seconds since the epoch"]))
#print(bytes_total(df["Response size in bytes"]))

res1 = bytes_total(df["Response size in bytes"])

save_results("Response size in bytes", res1)
#save_results(bytes_total(df["Response size in bytes"]))
