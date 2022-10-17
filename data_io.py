import os

from json import dump

import pandas as pd


# Input
def take_input_data(path: str) -> pd.DataFrame:

    if os.path.isfile(path):
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
    elif os.path.isdir(path):
        pass # TODO: add a directory concatenate script
    else:
        raise TypeError # TODO: add a specific message
    df = pd.DataFrame(data=file)
    return df


# Output
def save_results(col_name: str, result: str | int | float, path: str = "result.json"):
    json_dict = {f"{col_name}": f"{result}"}
    with open(path, "w") as fp:
        dump(json_dict, fp)
