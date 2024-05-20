# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from pydantic_xml import attr, element

from gvm_sync_targets.models.resource import (
    Count,
    Filters,
    Pagination,
    Resource,
    Sort,
)
from gvm_sync_targets.models.response import Response


class Task(Resource, tag="task"):
    pass


class GetTasksResponse(Response, tag="get_tasks_response"):
    tasks: list[Task] = element()
    filters: Filters
    sort: Sort
    pagination: Pagination = element("tasks")
    count: Count = element("task_count")


class DeleteTaskResponse(Response, tag="delete_task_response"):
    pass


class CreateTaskResponse(Response, tag="create_task_response"):
    uuid: str = attr("id")


class ModifyTaskResponse(Response, tag="modify_tag_response"):
    pass
