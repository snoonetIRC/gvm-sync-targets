# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import TYPE_CHECKING, TextIO, cast

import click
from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform

from gvm_sync_targets import __version__
from gvm_sync_targets.util import to_str

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
        elif target.xpath("sum(in_use/text()) > 0"):
            new_target = gmp.clone_target(to_str(target.attrib["id"]))
        else:
            new_target = target

        new_target_id: str = to_str(new_target.attrib["id"])
        # Set hosts
        # gmp.modify_target(new_target.attrib['id'], hosts=hosts)

        # Replace old target in tasks
        if target is not None and target is not new_target:
            old_target_id = to_str(target.attrib["id"])
            tasks = cast("ElementBase", gmp.get_tasks()).findall(
                f"task[target='{old_target_id}']"
            )

            for task in tasks:
                gmp.modify_task(
                    to_str(task.attrib["id"]), target_id=new_target_id
                )

            # Ensure old target is unused
            old_target: "ElementBase" = gmp.get_target(old_target_id)[0]
            old_name = old_target.xpath("name/text()[1]")
            if old_target.xpath("sum(in_use/text()) > 0"):
                msg = "target is still in use"
                raise ValueError(msg)

            # Delete old target
            gmp.delete_target(old_target_id, ultimate=True)

            # Rename new target
            gmp.modify_target(new_target_id, name=old_name)
