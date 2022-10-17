#!/usr/bin/python

import click

from data_io import save_results, take_input_data
from operations import bytes_total, e_ps, lf_ip, mf_ip


@click.group()
def analyse():
    pass


@analyse.command(name="mfip")
@click.option("--mfip", help="Most frequent IP")
@click.argument("input")
def mfip(mfip, input):
    df = take_input_data(input)
    mf = mf_ip(df)
    save_results("Most frequent IP", mf)


@analyse.command(name="lfip")
@click.option("--lfip", help="Least frequent IP")
@click.argument("input")
def lfip(lfip, input):
    df = take_input_data(input)
    lf = lf_ip(df)
    save_results("Least frequent IP", lf)


@analyse.command(name="eps")
@click.option("--eps", help="Events per second")
@click.argument("input")
def eps(eps, input):
    df = take_input_data(input)
    eps = e_ps(df)
    save_results("Events per second", eps)


@analyse.command(name="bytes")
@click.option("--bytes", help="Total amount of bytes exchanged")
@click.argument("input")
def bytes(bytes, input):
    df = take_input_data(input)
    bytes = bytes_total(df)
    save_results("Total amount of bytes exchanged", bytes)


if __name__ == "__main__":
    analyse()
