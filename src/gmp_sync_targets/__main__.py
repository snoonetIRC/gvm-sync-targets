# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from gmp_sync_targets.cli import gmp_sync_targets

    sys.exit(gmp_sync_targets())
