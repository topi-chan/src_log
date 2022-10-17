import mimetypes
import os
from json import dump

import pandas as pd


# Input
def take_input_data(path: str) -> pd.DataFrame:
    if (
        mimetypes.guess_type(path)[0] == "text/plain"
    ):  # If it's a single file with text type use this block to simply load a df
        df_data = pd.read_table(
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
    elif os.path.isdir(path):  # If it's a directory execute this block
        df_list = []  # Create an empty list of dataframes
        filelist = os.listdir(path)  # Make a list of files in the directory
        for file in filelist:  # Iterate through the file list
            if (
                mimetypes.guess_type(file)[0]
                == "text/plain"  # Check if file is of type 'text'
            ):
                df_list.append(  # Try to add a dataframe from file to a list
                    pd.read_table(
                        f"{path}/{file}",  # Make a filepath to specific file from base path + filename
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
                )
        df_data = pd.concat(df_list)  # Combine dataframes into one
    else:  # Return an error if neither plain text file nor directory is provided
        raise TypeError("You have to provide a plain text file or a directory.")
    df = pd.DataFrame(data=df_data)
    return df  # Return a dataframe either from single text file or block of text files


# Output
def save_results(col_name: str, result: str | int | float, path: str) -> None:
    json_dict = {f"{col_name}": f"{result}"}
    with open(path, "w") as fp:
        dump(json_dict, fp)
