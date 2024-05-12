# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT
import click
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp

from gvm_sync_targets import __version__


@click.group(
    context_settings={
        "help_option_names": ["-h", "--help"],
        "auto_envvar_prefix": "GVM",
    },
    invoke_without_command=True,
)
@click.version_option(version=__version__, prog_name="gvm-sync-targets")
@click.option("--username", show_envvar=True)
@click.option("--password", show_envvar=True)
def gvm_sync_targets(username: str, password: str) -> None:
    with Gmp(UnixSocketConnection()) as gmp:
        gmp.authenticate(username, password)
        for target in gmp.get_targets():
            print(target)
            print(type(target))
            for k in dir(target):
                print(k, getattr(target, k))
