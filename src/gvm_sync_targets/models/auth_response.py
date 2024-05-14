# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from pydantic_xml import element

from gvm_sync_targets.models.response import Response


class AuthenticateResponse(Response, tag="authenticate_response"):
    role: str = element()
    timezone: str = element()
