import mimetypes
import os
from json import dump

import pandas as pd


PD_COLUMN_NAMES = [
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
]


def read_table(path: str) -> pd.DataFrame:
    df_data = pd.read_table(
        path,
        on_bad_lines="skip",
        sep=" ",
        skipinitialspace=True,
        names=PD_COLUMN_NAMES,
    )
    return df_data


# Input
def load_input_data(path: str) -> pd.DataFrame:
    if (
        mimetypes.guess_type(path)[0] == "text/plain"
    ):  # If it's a single file with detectable text type use this block to simply load a df
        df_data = read_table(path)
    elif os.path.isdir(path):  # If it's a directory execute this block
        df_list = []  # Create an empty list of dataframes
        filelist = os.listdir(path)  # Make a list of files in the directory
        for file in filelist:  # Iterate through the file list
            try:  # Try-except in case there are mixed type files in directory, e.g. binary
                df_list.append(  # Try to add a dataframe from file to a list
                    read_table(
                        f"{path}/{file}"  # Make a filepath to specific file from base path + filename
                    )
                )
            except Exception as e:  # Print why type can't be processed and continue iteration
                print(f"Can not handle file. Error log: {e}")
                continue
        if filelist:
            df_data = pd.concat(df_list)  # Combine dataframes into one
        else:  # If filelist was empty try to create a single dataframe
            df_data = read_table(path)
    else:
        try:  # Last try, if datatype not detected
            df_data = read_table(path)
        # Return an error if neither plain text file nor directory is provided and there's no file that can be processed
        except Exception as e:
            raise TypeError(
                f"You have to provide a plain text file or a directory. Error log: {e}"
            )
    df = pd.DataFrame(data=df_data)
    return df  # Return a dataframe either from single text file or block of text files


# Output
def save_results(col_name: str, result: str | int | float, path: str) -> None:
    json_dict = {f"{col_name}": f"{result}"}  # Create dictionary with analysis result
    with open(path, "w") as fp:
        dump(json_dict, fp)  # Save dict as json file
