# Copyright 2020 The SQLFlow Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from runtime.step.tensorflow.local_test_base import \
    TestTensorFlowLocalSubmitter


class TestKeras(TestTensorFlowLocalSubmitter):
    def test_main(self):
        self.check_main('sqlflow_models.DNNClassifier')


if __name__ == '__main__':
    unittest.main()