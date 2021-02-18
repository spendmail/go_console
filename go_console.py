#!/usr/bin/env python3
import os
import pathlib
import sys
import click

GO_DIRS = ['api', 'cmd', 'pkg', 'internal/domain/errors', 'internal/domain/interfaces', 'internal/domain/models',
           'internal/domain/services', 'internal/adapters/grpc/api', 'internal/adapters/maindb', 'sql']


@click.group()
@click.version_option("0.0.1")
def main():
    """Go Console Instruments"""
    pass


@main.command()
@click.argument('path', required=False)
def make_project(path):
    """Makes go project standard dirs"""

    if path is None:
        path = os.getcwd()

    if not os.path.exists(path):
        pathlib.Path(path)

    for go_dir in GO_DIRS:
        pathlib.Path(os.path.join(path, go_dir)).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    args = sys.argv
if "--help" in args or len(args) == 1:
    print("CVE")
main()
