# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

import logging
from typing import Optional, TextIO, cast

import click
from gvm.connections import DebugConnection, UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform

from gvm_sync_targets import __version__
from gvm_sync_targets.models import ModelTransform
from gvm_sync_targets.models.assets_response import GetAssetsResponse
from gvm_sync_targets.util import Element, target_in_use, to_str


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
@click.option(
    "--debug", is_flag=True, default=False, help="Enable debug logging"
)
@click.argument("hosts_file", type=click.File())
def gvm_sync_targets(
    username: str, password: str, debug: bool, hosts_file: TextIO
) -> None:
    if debug:
        logging.basicConfig(level="DEBUG", force=True)

    with Gmp(
        DebugConnection(UnixSocketConnection()),
        transform=ModelTransform(),
    ) as gmp:
        hosts = hosts_file.read().splitlines()
        gmp.authenticate(username, password)
        existing_hosts: GetAssetsResponse = gmp.get_hosts(details=True)
        to_add = hosts.copy()
        to_remove: list[str] = []

        for host in existing_hosts.assets:
            ips = {
                identifier.value
                for identifier in host.identifiers.identifiers
                if identifier.name == "ip"
            }

            if len(ips) > 1:
                raise ValueError(f"Multiple IPs?: {ips}")

            for ip in ips:
                if ip in to_add:
                    to_add.remove(ip)
                elif ip not in hosts:
                    to_remove.append(host.uuid)

        for ip in to_add:
            gmp.create_host(ip)

        for uuid in to_remove:
            gmp.delete_host(uuid)

    click.echo(f"Added {len(to_add)} hosts, removed {len(to_remove)}.")
