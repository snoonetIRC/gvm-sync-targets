# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

import datetime
from typing import Optional

from pydantic_xml import attr, element

from gvm_sync_targets.models.model import IntBoolean, Model


class Owner(Model, tag="owner"):
    name: str = element()


class Permission(Model, tag="permission"):
    name: str = element()


class Permissions(Model, tag="permissions"):
    permissions: list[Permission] = element()


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


class Count(Model):
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


class Resource(Model):
    uuid: str = attr("id")

    owner: Owner
    name: str = element()
    comment: Optional[str] = element(default=None)
    creation_time: datetime.datetime = element()
    modification_time: datetime.datetime = element()
    writable: IntBoolean = element()
    in_use: IntBoolean = element()

    permissions: Permissions = element()
