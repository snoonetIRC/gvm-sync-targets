# SPDX-FileCopyrightText: 2024-present linuxdaemon <linuxdaemon.irc@gmail.com>
#
# SPDX-License-Identifier: MIT

from collections.abc import Mapping
from typing import cast

from gvm.transforms import EtreeCheckCommandTransform

from gvm_sync_targets.models.assets_response import (
    CreateAssetResponse,
    DeleteAssetResponse,
    GetAssetsResponse,
)
from gvm_sync_targets.models.auth_response import AuthenticateResponse
from gvm_sync_targets.models.response import Response
from gvm_sync_targets.models.targets_response import GetTargetsResponse
from gvm_sync_targets.util import Element

__all__ = [
    "GetAssetsResponse",
    "AuthenticateResponse",
    "DeleteAssetResponse",
    "CreateAssetResponse",
    "GetTargetsResponse",
]

_MODEL_MAP: Mapping[str, type[Response]] = {
    "get_assets_response": GetAssetsResponse,
    "authenticate_response": AuthenticateResponse,
    "delete_asset_response": DeleteAssetResponse,
    "create_asset_response": CreateAssetResponse,
    "get_targets_response": GetTargetsResponse,
}


class ModelTransform(EtreeCheckCommandTransform):
    def __init__(self) -> None:
        super().__init__()  # type: ignore[no-untyped-call]

    def __call__(self, data: str) -> Response:
        elem = cast(Element, super().__call__(data))
        return _MODEL_MAP[elem.tag].from_xml_tree(elem)  # type: ignore[arg-type] # etree.Element isn't a type but that's what this function expects
