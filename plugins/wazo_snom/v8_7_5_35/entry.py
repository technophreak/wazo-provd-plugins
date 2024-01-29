# Copyright 2014-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypedDict

    from ..common.common import BaseSnomPgAssociator, BaseSnomPlugin  # noqa: F401

    class CommonGlobalsDict(TypedDict):
        BaseSnomPlugin: type[BaseSnomPlugin]
        BaseSnomPgAssociator: type[BaseSnomPgAssociator]


common_globals: CommonGlobalsDict = {}  # type: ignore[typeddict-item]
execfile_('common.py', common_globals)  # type: ignore[name-defined]

MODELS = [
    '300',
    '320',
    '370',
    '710',
    '715',
    '720',
    '725',
    '760',
    'D765',
    '820',
    '821',
    '870',
    'MP',
    'PA1',
]
VERSION = '8.7.5.35'


class SnomPlugin(common_globals['BaseSnomPlugin']):  # type: ignore[valid-type,misc]
    IS_PLUGIN = True

    _MODELS = MODELS

    pg_associator = common_globals['BaseSnomPgAssociator'](MODELS, VERSION)
