from tkinter import W
import click

import pyfiledb


@click.group()
def cli():
    pass


@cli.command()
def add():
    filedb = pyfiledb.pyfiledb()
    path = input('path: ')
    hashs = input('hashs: ')
    filedb.append(path, hashs)
    filedb.close()


@cli.command()
def search():
    filedb = pyfiledb.pyfiledb()
    hashs = input('hashs: ')
    reslut = filedb.search(hashs)
    for i, key in enumerate(reslut):
        click.echo(f'-[{i}]-------------')
        click.echo(f'path: {key}')
        click.echo(f'hashs: {reslut[key]}')
        click.echo('')
    filedb.close()


cli()
