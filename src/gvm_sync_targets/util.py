# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import TYPE_CHECKING

from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from lxml.etree import _Element

Element: TypeAlias = "_Element"

__all__ = [
    "Element",
    "read_lines",
]


def read_lines(data: str, ignore_comments: bool = True) -> list[str]:
    return [
        line
        for line in data.splitlines()
        if not (ignore_comments and line.lstrip().startswith("#"))
    ]
