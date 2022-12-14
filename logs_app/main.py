#!/usr/bin/python

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from time import sleep

import click
import pandas as pd
from rich.console import Console

from logs_app.data_io import load_input_data, save_results
from logs_app.operations import bytes_total, e_ps, lf_ip, mf_ip


console = Console()

# Helper block in case of someone opening the app without any argument, such --help or actual command
if __name__ == "__main__":
    if len(sys.argv) > 1:
        pass
    else:
        console.print("[red]You have to add an argument, type python main.py --help for instructions.[red]")
        quit()

# Show full help message if --help is used
if __name__ == "__main__" and sys.argv[1] == "--help":
    console.print(
        """Hi :vampire:\n[b][i]This is a console log analyzer program[/i]\nIs has four operations.
        \nIt takes an operation type argument, then location of file or a directory with logs, then directory to save result
        \nTo use it run a command for a operation as specified below
        \nInput file/files should be of plain-text type and output file of json type.\n"""
    )


# Load data from file and display console message
def base_task(input: str) -> pd.DataFrame:
    tasks = ["read file", "prepare file", "analyze and save file"]
    with console.status("[bold green]Working on tasks..."):
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task}")
    df = load_input_data(input)
    return df


# Execution of each command: 1/load data (logic from data_io module) 2/analyze it (operations module) 3/ save (data_io)
@click.group()
def analyze_logs():
    pass


@analyze_logs.command(name="mfip")
@click.option(
    "--mfip",
    help=console.print(
        "[bold magenta]Most frequent IP.[/bold magenta]",
        "\nUse: [b]python main.py mfil[b] <input_file/dir> <output_file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def mfip(mfip, input, output):
    df = base_task(input)
    mf = mf_ip(df)
    save_results("Most frequent IP", mf, output)
    console.print(
        f"\n\n[i][b][bold magenta]Most frequent IP determined and saved in: {output}.[/bold magenta][b][i]"
    )


@analyze_logs.command(name="lfip")
@click.option(
    "--lfip",
    help=console.print(
        "[bold magenta]Least frequent IP.[bold magenta]",
        "\nUse: [b]python main.py lfip[b] <input_file/dir> <output_file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def lfip(lfip, input, output):
    df = base_task(input)
    lf = lf_ip(df)
    save_results("Least frequent IP", lf, output)
    console.print(
        f"\n\n[i][b][bold magenta]Least frequent IP determined and saved in: {output}.[/bold magenta][b][i]"
    )


@analyze_logs.command(name="eps")
@click.option(
    "--eps",
    help=console.print(
        "[bold magenta]Events per second.[bold magenta]",
        "\nUse: [b]python main.py eps[b] <input_file/dir> <output_file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def eps(eps, input, output):
    df = base_task(input)
    eps = e_ps(df)
    save_results("Events per second", eps, output)
    console.print(
        f"\n\n[i][b][bold magenta]Events per second counted and saved in: {output}.[/bold magenta][b][i]"
    )


@analyze_logs.command(name="bytes")
@click.option(
    "--bytes",
    help=console.print(
        "[bold magenta]Total amount of bytes exchanged.[bold magenta]",
        "\nUse: [b]python main.py bytes[b] <input_file/dir> <output_file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def bytes(bytes, input, output):
    df = base_task(input)
    bytes = bytes_total(df)
    save_results("Total amount of bytes exchanged", bytes, output)
    console.print(
        f"\n\n[i][b][bold magenta]Total amount of bytes exchanged counted and saved in: {output}.[/bold magenta][b][i]"
    )


if __name__ == "__main__":
    analyze_logs()
