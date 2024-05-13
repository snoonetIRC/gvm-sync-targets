# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from pydantic_xml import attr

from gvm_sync_targets.models.model import Model


class Response(Model):
    status: int = attr()
    status_text: str = attr()
