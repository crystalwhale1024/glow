# Copyright (c) Glow Contributors. See CONTRIBUTORS file.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pyre-ignore-all-errors

from __future__ import absolute_import, division, print_function, unicode_literals

import torch
from tests import utils


class SimplePermuteModule(torch.nn.Module):
    def __init__(self, *dimensions):
        super(SimplePermuteModule, self).__init__()
        self.dimensions = dimensions

    def forward(self, tensor):
        return tensor.permute(*self.dimensions)


class TestPermute(utils.TorchGlowTestCase):
    def test_permute(self):
        """Basic test of the PyTorch aten::permute node on Glow."""

        utils.compare_tracing_methods(
            SimplePermuteModule(0, 2, 1),
            torch.randn(2, 3, 4),
            fusible_ops={"aten::permute"},
        )
