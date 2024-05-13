# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from gvm_sync_targets.models.auth_response import AuthenticateResponse

data = """
<authenticate_response status="200" status_text="OK">
    <role>Admin</role>
    <timezone>UTC</timezone>
</authenticate_response>
"""


def test_auth_response() -> None:
    model = AuthenticateResponse.from_xml(data)
    assert model.role == "Admin"
    assert model.timezone == "UTC"
