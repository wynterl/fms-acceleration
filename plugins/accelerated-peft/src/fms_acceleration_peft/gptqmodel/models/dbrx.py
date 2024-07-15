###############################################################################
# Adapted from https://github.com/ModelCloud/GPTQModel
#
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
###############################################################################
# Local
from .base import BaseGPTQModel


# placer=holder only as dbrx original models are not supported
# supported dbrx_converted models can be found on https://hf.co/ModelCloud
class DbrxGPTQ(BaseGPTQModel):
    info = {
        "notes": "Dbrx is only supported using defused/converted models on https://hf.co/ModelCloud with `trust_remote_code=True`"
    }
