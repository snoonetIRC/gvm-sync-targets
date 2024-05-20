# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

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


class Credential(Model):
    uuid: str = attr("id")
    name: str | None = element(default=None)

    trash: IntBoolean = element(tag="trash")


class SSHCredential(Credential, tag="ssh_credential"):
    port: int = element(tag="port")


class SMBCredential(Credential, tag="smb_credential"):
    pass


class ESXICredential(Credential, tag="esxi_credential"):
    pass


class SNMPCredential(Credential, tag="snmp_credential"):
    pass


class SSHElevateCredential(Credential, tag="ssh_elevate_credential"):
    pass


class PortList(Model, tag="port_list"):
    uuid: str = attr("id")

    name: str = element()
    trash: IntBoolean = element()


class Task(Resource, tag="task"):
    uuid: str = attr("id")

    name: str = element()


class Tasks(Resource, tag="tasks"):
    tasks: list[Task] = element()


class Target(Resource, tag="target"):
    hosts: str = element()
    exclude_hosts: str | None = element(default=None)
    max_hosts: int = element()
    port_list: PortList = element()
    ssh_credential: SSHCredential = element()
    smb_credential: SMBCredential = element()
    esxi_credential: ESXICredential = element()
    snmp_credential: SNMPCredential = element()
    ssh_elevate_credential: SSHElevateCredential = element()

    reverse_lookup_only: IntBoolean = element()
    reverse_lookup_unify: IntBoolean = element()
    alive_tests: str = element()
    allow_simultaneous_ips: IntBoolean = element()
    tasks: Tasks = element()


class GetTargetsResponse(Response, tag="get_targets_response"):
    targets: list[Target] = element()
    filters: Filters
    sort: Sort
    pagination: Pagination = element("targets")
    asset_count: Count = element("target_count")


class DeleteTargetResponse(Response, tag="delete_target_response"):
    pass


class CreateTargetResponse(Response, tag="create_target_response"):
    uuid: str = attr("id")
