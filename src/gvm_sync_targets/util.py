# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import TYPE_CHECKING, Union

from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from lxml.etree import _Element

Element: TypeAlias = "_Element"

__all__ = [
    "to_str",
    "target_in_use",
    "Element",
]


def to_str(text: Union[str, bytes, bytearray, memoryview]) -> str:
    """Convert bytes, bytearray, memoryview, or str to str.

    Args:
        text: Input value

    Returns:
        decoded output

    Examples:
        >>> to_str("aaa")
        'aaa'
        >>> to_str(b'bb')
        'bb'
        >>> to_str(memoryview(b'bb'))
        'bb'
        >>> to_str(bytearray(b'cc'))
        'cc'
    """
    if isinstance(text, (bytes, bytearray)):
        return text.decode()

    if isinstance(text, memoryview):
        return to_str(text.tobytes())

    return text


def target_in_use(target: Element) -> bool:
    return bool(target.xpath("boolean(in_use[text()='1'])"))
