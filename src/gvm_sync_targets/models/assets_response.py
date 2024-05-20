# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

import datetime

from pydantic_xml import attr, element

from gvm_sync_targets.models.model import IntBoolean, Model
from gvm_sync_targets.models.resource import (
    Count,
    Filters,
    Pagination,
    Resource,
    Sort,
)
from gvm_sync_targets.models.response import Response


class Severity(Model, tag="severity"):
    value: float | None = element(default=None)


class Source(Model, tag="source"):
    uuid: str = attr("id")

    type: str = element()
    data: str | None = element(default=None)
    deleted: IntBoolean = element(default=False)
    name: str | None = element(default=None)


class Detail(Model, tag="detail"):
    name: str = element()
    value: str = element()
    source: Source = element()


class Host(Model, tag="host"):
    severity: Severity = element()
    details: list[Detail] = element("detail", default_factory=list)


class Tag(Model, tag="tag"):
    uuid: str = attr("id")

    name: str = element()
    value: str = element()


class UserTags(Model, tag="user_tags"):
    count: int = element()
    tags: list[Tag] = element()


class OS(Model, tag="os"):
    uuid: str = attr("id")

    title: str = element()


class Identifier(Model, tag="identifier"):
    uuid: str = attr("id")

    name: str = element()
    value: str = element()
    creation_time: datetime.datetime = element()
    modification_time: datetime.datetime = element()

    source: Source | None = None
    os: OS | None = None


class Identifiers(Model, tag="identifiers"):
    identifiers: list[Identifier] = element()


class Asset(Resource, tag="asset"):
    user_tags: UserTags | None = element(default=None)
    identifiers: Identifiers = element()
    type: str = element()
    host: Host = element("host")


class GetAssetsResponse(Response, tag="get_assets_response"):
    assets: list[Asset] = []
    filters: Filters
    sort: Sort
    pagination: Pagination = element("assets")
    count: Count = element("asset_count")


class DeleteAssetResponse(Response, tag="delete_asset_response"):
    pass


class CreateAssetResponse(Response, tag="create_asset_response"):
    uuid: str = attr("id")


class ModifyAssetResponse(Response, tag="modify_asset_response"):
    pass
