# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import Union


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
