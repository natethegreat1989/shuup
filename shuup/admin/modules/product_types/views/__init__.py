# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2019, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from .delete import ProductTypeDeleteView
from .edit import ProductTypeEditView
from .list import ProductTypeListView

__all__ = [
    "ProductTypeEditView",
    "ProductTypeListView",
    "ProductTypeDeleteView"
]
