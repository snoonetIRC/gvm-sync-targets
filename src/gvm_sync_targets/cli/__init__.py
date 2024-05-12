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
        transform=EtreeCheckCommandTransform(),
    ) as gmp:
        hosts = hosts_file.read().splitlines()
        gmp.authenticate(username, password)
        targets: Element = gmp.get_targets()
        target: Optional[Element] = targets.find("target[name='All Hosts']")

        if target is None:
            # Create target
            new_target = gmp.create_target("All Hosts")
        elif target_in_use(target):
            new_target = gmp.clone_target(to_str(target.attrib["id"]))
        else:
            new_target = target

        new_target_id: str = to_str(new_target.attrib["id"])
        # Set hosts
        # gmp.modify_target(new_target.attrib['id'], hosts=hosts)

        # Replace old target in tasks
        if target is not None and target is not new_target:
            old_target_id = to_str(target.attrib["id"])
            task_ids = cast(
                list[str],
                cast(Element, gmp.get_tasks()).xpath(
                    f"task[target/@id='{old_target_id}']/@id"
                ),
            )

            for task_id in task_ids:
                gmp.modify_task(task_id, target_id=new_target_id)

            # Ensure old target is unused
            old_target: Element = gmp.get_target(old_target_id)[0]
            old_name = cast(list[str], old_target.xpath("name/text()"))[0]
            if target_in_use(old_target):
                msg = "target is still in use"
                raise ValueError(msg)

            # Delete old target
            gmp.delete_target(old_target_id, ultimate=True)

            # Rename new target
            gmp.modify_target(new_target_id, name=old_name)
