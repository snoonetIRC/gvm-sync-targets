# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Mapping
from typing import Type, cast

from gvm.transforms import EtreeCheckCommandTransform

from gvm_sync_targets.models.assets_response import GetAssetsResponse
from gvm_sync_targets.models.model import Model
from gvm_sync_targets.util import Element

_MODEL_MAP: Mapping[str, type[Model]] = {
    "get_assets_response": GetAssetsResponse,
}


class ModelTransform(EtreeCheckCommandTransform):
    def __init__(self) -> None:
        super().__init__()  # type: ignore[no-untyped-call]

    def __call__(self, data: str) -> Model:
        elem = cast(Element, super().__call__(data))
        return _MODEL_MAP[elem.tag].from_xml_tree(elem)  # type: ignore[arg-type] # etree.Element isn't a type but that's what this function expects
