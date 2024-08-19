# -*- coding: utf-8 -*-
#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/aboutcode-org/scancode-toolit for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import click
import json
import os


def load_json(path):
    with open(path, 'r') as file_handler:
        data = json.load(file_handler)
    return data


def write_json(data, path):
    with open(path, 'w') as file_handler:
        json.dump(data, file_handler, indent=2)


class NoNewCommitException(Exception):
    pass


@click.command()
@click.option('--commit',
              type=click.STRING,
              default=None,
              metavar='FILE',
              )
def cli(commit):
    """
    Check if the commit `commit` at which the licensedb was last generated
    and verify whether there are new commits.

    - If there are new commits, write the last commit has to last_commit.json
    - If there are no new commits, fail loudly.
    """
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "last_commit.json"
    )

    data_commit_old = load_json(path=path)
    commit_old = data_commit_old["commit_hash"]

    msg = (
        f"There are no new commits in scancode-toolkit develop after {commit_old}."
        "Aborting LicenseDB update."
    )

    if commit == commit_old:
        raise NoNewCommitException(msg)
    else:
        click.secho(
            f" -> There are new commits in scancode-toolkit develop, updating last commit to {commit}.")
        data_commit_old["commit_hash"] = commit
        write_json(data=data_commit_old, path=path)


if __name__ == '__main__':
    cli()
