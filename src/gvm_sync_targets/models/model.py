# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from typing import Annotated

from pydantic import PlainSerializer
from pydantic_xml import BaseXmlModel

IntBoolean = Annotated[
    bool, PlainSerializer(lambda value: 1 if value else 0, return_type=int)
]


class Model(BaseXmlModel, search_mode="unordered", extra="forbid"):
    pass
