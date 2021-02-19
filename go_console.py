#!/usr/bin/env python3
import glob
import ntpath
import os
import pathlib
import sys
import click

GO_DIRS = ['api', 'cmd', 'pkg', 'internal/domain/errors', 'internal/domain/interfaces', 'internal/domain/models',
           'internal/domain/services', 'internal/adapters/grpc/api', 'internal/adapters/maindb', 'sql']

README = '''# Project Name

# Build and run the Docker image
    $ docker build -t my-golang-app .
    $ docker run -it --rm --name my-running-app my-golang-app
'''

DOCKERFILE = '''FROM golang:1.14

WORKDIR /go/src/app
COPY . .

RUN go get -d -v ./...
RUN go install -v ./...

CMD ["app"]'''

ENV = '''APP_ENV=prod
#DATABASE_URL=pgsql://user:pass@localhost:5432/db
'''

GO_FILES = {'README.md': README, 'DOCKERFILE': README, '.env': ENV}


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

    for go_file in GO_FILES:
        readme_path = os.path.join(path, go_file)
        if not os.path.exists(readme_path):
            with open(readme_path, 'a') as f:
                f.write(GO_FILES[go_file])


@main.command()
@click.argument('path', required=False)
def make_tests(path):
    """Creates go project test files"""

    if path is None:
        path = os.getcwd()

    services_path = os.path.join(path, 'internal/domain/services')
    if not os.path.exists(services_path):
        return

    for file in glob.glob(services_path + '/*.go'):
        file = pathlib.Path(file)
        test_filename = file.stem + '_test' + file.suffix
        test_abs_name = os.path.join(services_path, test_filename)
        if not os.path.exists(test_abs_name):
            with open(test_abs_name, 'a') as f:
                f.write('')


if __name__ == '__main__':
    args = sys.argv
if "--help" in args or len(args) == 1:
    print("CVE")
main()
