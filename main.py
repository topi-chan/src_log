#!/usr/bin/python
import sys

import click
from rich.console import Console

from data_io import load_input_data, save_results
from operations import bytes_total, e_ps, lf_ip, mf_ip

console = Console()


if sys.argv[1] == "--help":
    console.print(
        """Hi :vampire:\n[b][i]This is a console log analyzer program[/i]\nIs has four operations.
        \nIt takes an operation type argument, then location of file or a directory with logs, then directory to save result
        \nTo use it run a command for a operation as specified below."""
    )


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
    df = load_input_data(input)
    mf = mf_ip(df)
    save_results("Most frequent IP", mf, output)
    console.print(
        f"\n\ni][b][bold magenta]Most frequent IP determined and saved in: {output}.[/bold magenta][b][i]")


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
    df = load_input_data(input)
    lf = lf_ip(df)
    save_results("Least frequent IP", lf, output)
    console.print(
        f"\n\n[i][b][bold magenta]Least frequent IP determined and saved in: {output}.[/bold magenta][b][i]")


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
    df = load_input_data(input)
    eps = e_ps(df)
    save_results("Events per second", eps, output)
    console.print(
        f"\n\n[i][b][bold magenta]Events per second counted and saved in: {output}.[/bold magenta][b][i]")


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
    df = load_input_data(input)
    bytes = bytes_total(df)
    save_results("Total amount of bytes exchanged", bytes, output)
    console.print(
        f"\n\n[i][b][bold magenta]Total amount of bytes exchanged counted and saved in: {output}.[/bold magenta][b][i]")


if __name__ == "__main__":
    analyze_logs()
