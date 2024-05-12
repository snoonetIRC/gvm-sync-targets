# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT
from click.testing import CliRunner

import gvm_sync_targets
from gvm_sync_targets import cli


def test_gvm_sync_targets() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.gvm_sync_targets, ["--version"])
    assert result.exit_code == 0
    assert (
        result.output
        == f"gvm-sync-targets, version {gvm_sync_targets.version}\n"
    )
