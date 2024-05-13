# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from pydantic_xml import BaseXmlModel


class Model(BaseXmlModel, extra="forbid"):
    pass
