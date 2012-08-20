# python-either
# Homepage: https://github.com/kennknowles/python-either
#
# Copyright 2012- Kenneth Knowles
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


class Either(object):
    pass

class Left(Either):
    def __init__(self, v): self.v = v
    def is_left(self): return True
    def is_right(self): return False
    def value(self): return self.v 

class Right(Either):
    def __init__(self, v): self.v = v
    def is_left(self): return False
    def is_right(self): return True
    def value(self): return self.v 


class Maybe(object):
    pass

class Nothing(Maybe):
    def is_empty(self): return True
    def is_something(self): return False
    def value(self): raise Exception('Called value() on Nothing value')

class Something(Maybe):
    def __init__(self, v): self.v = v
    def is_empty(self): return False
    def is_something(self): return True
    def value(self): return self.v
