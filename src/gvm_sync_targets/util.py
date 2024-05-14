# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Generator
from typing import TYPE_CHECKING, Optional

from gvm.protocols.gmpv208.entities.hosts import HostsMixin
from typing_extensions import TypeAlias

from gvm_sync_targets.models.assets_response import Asset, GetAssetsResponse

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


def get_all_hosts(
    proto: HostsMixin,
    filter_string: Optional[str] = None,
    filter_id: Optional[str] = None,
    details: Optional[bool] = None,
) -> Generator[Asset, None, None]:
    first: GetAssetsResponse = proto.get_hosts(
        filter_string=filter_string,
        filter_id=filter_id,
        details=details,
    )

    item: GetAssetsResponse = first
    yield from item.assets
    starting_index = 1
    while starting_index < item.asset_count.filtered:
        keywords = item.filters.keywords.keywords
        filter_string = " ".join(
            f"{kw.column}{kw.relation}{kw.value}"
            for kw in keywords
            if kw.column != "first"
        )

        starting_index = item.pagination.start + item.asset_count.page

        if filter_string:
            filter_string = f"first={starting_index} {filter_string}"
        else:
            filter_string = f"first={starting_index}"

        item = proto.get_hosts(
            filter_string=filter_string,
            filter_id=filter_id,
            details=details,
        )

        yield from item.assets
