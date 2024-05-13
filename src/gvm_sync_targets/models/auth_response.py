# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from pydantic_xml import attr, element

from gvm_sync_targets.models.model import Model


class AuthenticateResponse(Model, tag="authenticate_response"):
    status: int = attr("status")
    status_text: str = attr("status_text")

    role: str = element()
    timezone: str = element()
