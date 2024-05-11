# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from gvm_sync_targets.cli import gvm_sync_targets

    sys.exit(gvm_sync_targets())
