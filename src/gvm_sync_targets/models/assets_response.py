# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

import datetime
from typing import Annotated, Optional

from pydantic import PlainSerializer
from pydantic_xml import attr, element

from gvm_sync_targets.models.model import Model
from gvm_sync_targets.models.response import Response

IntBoolean = Annotated[
    bool, PlainSerializer(lambda value: 1 if value else 0, return_type=int)
]


class Severity(Model, tag="severity"):
    value: Optional[float] = element(default=None)


class Source(Model, tag="source"):
    uuid: str = attr("id")

    type: str = element()
    data: Optional[str] = element(default=None)
    deleted: IntBoolean = element(default=False)
    name: Optional[str] = element(default=None)


class Detail(Model, tag="detail"):
    name: str = element()
    value: str = element()
    source: Source = element()


class Host(Model, tag="host"):
    severity: Severity = element()
    details: list[Detail] = element("detail", default_factory=list)


class Owner(Model, tag="owner"):
    name: str = element()


class Permission(Model, tag="permission"):
    name: str = element()


class Permissions(Model, tag="permissions"):
    permissions: list[Permission] = element()


class OS(Model, tag="os"):
    uuid: str = attr("id")

    title: str = element()


class Identifier(Model, tag="identifier"):
    uuid: str = attr("id")

    name: str = element()
    value: str = element()
    creation_time: datetime.datetime = element()
    modification_time: datetime.datetime = element()

    source: Optional[Source] = None
    os: Optional[OS] = None


class Identifiers(Model, tag="identifiers"):
    identifiers: list[Identifier] = element()


class Asset(Model, tag="asset"):
    uuid: str = attr("id")

    owner: Owner
    name: str = element()
    comment: Optional[str] = element(default=None)
    creation_time: datetime.datetime = element()
    modification_time: datetime.datetime = element()
    writable: IntBoolean = element()
    in_use: IntBoolean = element()

    permissions: Permissions = element()
    identifiers: Identifiers = element()
    type: str = element()
    host: Host = element("host")


class Keyword(Model, tag="keyword"):
    column: str = element()
    relation: str = element()
    value: str = element()


class Keywords(Model, tag="keywords"):
    keywords: list[Keyword] = element()


class Filters(Model, tag="filters"):
    uuid: str = attr("id")

    term: str = element()
    keywords: Keywords = element()


class AssetCount(Model, tag="asset_count"):
    total: int
    filtered: int = element()
    page: int = element()


class Pagination(Model):
    start: int = attr()
    max: int = attr()


class SortField(Model, tag="field"):
    name: str
    order: str = element()


class Sort(Model, tag="sort"):
    field: SortField


class GetAssetsResponse(Response, tag="get_assets_response"):
    assets: list[Asset] = []
    filters: Filters
    sort: Sort
    pagination: Pagination = element("assets")
    asset_count: AssetCount


class DeleteAssetResponse(Response, tag="delete_asset_response"):
    pass


class CreateAssetResponse(Response, tag="create_asset_response"):
    uuid: str = attr("id")
