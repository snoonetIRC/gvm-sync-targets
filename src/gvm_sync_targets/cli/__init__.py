# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import TYPE_CHECKING, Optional, TextIO

import click
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform

from gvm_sync_targets import __version__

if TYPE_CHECKING:
    from lxml.etree import ElementBase


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
@click.argument("hosts_file", type=click.File())
def gvm_sync_targets(username: str, password: str, hosts_file: TextIO) -> None:
    with Gmp(
        UnixSocketConnection(), transform=EtreeCheckCommandTransform()
    ) as gmp:
        hosts = hosts_file.read().splitlines()
        gmp.authenticate(username, password)
        targets: "ElementBase" = gmp.get_targets()
        target = targets.find("target[name='All Hosts']")

        if target is None:
            # Create target
            new_target = gmp.create_target("All Hosts")
        elif target.xpath("in_use/text()") == ["1"]:
            new_target = gmp.clone_target(target.attrib["id"])
        else:
            new_target = target

        # Set hosts
        # gmp.modify_target(new_target.attrib['id'], hosts=hosts)

        # Replace old target in tasks
        if target is not None and target is not new_target:
            tasks = gmp.get_tasks().findall("task")
            if tasks is None:
                tasks = []

            for task in tasks:
                print(task)
                print(task.attrib)
                for child in task:
                    print(child)
                    print(child.attrib)

            # Ensure old target is unused
            # Delete old target
            # Rename new target
