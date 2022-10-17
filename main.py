#!/usr/bin/python

import click
from rich.console import Console

from data_io import save_results, take_input_data
from operations import bytes_total, e_ps, lf_ip, mf_ip


@click.group()
def analyze_logs():
    pass


console = Console()


@analyze_logs.command(name="mfip")
@click.option(
    "--mfip",
    help=console.print(
        "[bold magenta]Most frequent IP.[/bold magenta]",
        "\nUse: python main.py mfil <input file/dir> <output file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def mfip(mfip, input, output):
    df = take_input_data(input)
    mf = mf_ip(df)
    save_results("Most frequent IP", mf, output)


@analyze_logs.command(name="lfip")
@click.option(
    "--lfip",
    help=console.print(
        "[bold magenta]Least frequent IP.[bold magenta]",
        "\nUse: python main.py lfip <input file/dir> <output file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def lfip(lfip, input, output):
    df = take_input_data(input)
    lf = lf_ip(df)
    save_results("Least frequent IP", lf, output)


@analyze_logs.command(name="eps")
@click.option(
    "--eps",
    help=console.print(
        "[bold magenta]Events per second.[bold magenta]",
        "\nUse: python main.py eps <input file/dir> <output file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def eps(eps, input, output):
    df = take_input_data(input)
    eps = e_ps(df)
    save_results("Events per second", eps, output)


@analyze_logs.command(name="bytes")
@click.option(
    "--bytes",
    help=console.print(
        "[bold magenta]Total amount of bytes exchanged.[bold magenta]",
        "\nUse: python main.py bytes <input file/dir> <output file>",
    ),
    metavar="",
)
@click.argument("input")
@click.argument("output")
def bytes(bytes, input, output):
    df = take_input_data(input)
    bytes = bytes_total(df)
    save_results("Total amount of bytes exchanged", bytes, output)


if __name__ == "__main__":
    analyze_logs()
