#!/usr/bin/env python3
import os
import pathlib
import sys
import click


@click.group()
@click.version_option("0.0.1")
def main():
    """Go Console Instruments"""
    pass


@main.command()
@click.argument('path', required=False)
def make_dirs(path):
    """Makes go project standard dirs"""

    if path is None:
        path = os.getcwd()

    if not os.path.exists(path):
        pathlib.Path(path)

    pathlib.Path(os.path.join(path, "api")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "cmd")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "pkg")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "internal/domain/errors")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "internal/domain/interfaces")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "internal/domain/models")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "internal/domain/services")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "internal/adapters/grpc/api")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "internal/adapters/maindb")).mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(path, "sql")).mkdir(parents=True, exist_ok=True)

    pass


if __name__ == '__main__':
    args = sys.argv
if "--help" in args or len(args) == 1:
    print("CVE")
main()
