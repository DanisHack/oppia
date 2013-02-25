# coding: utf-8
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Normalizers and validators for various inputs (assumed to be strings)."""

__author__ = 'Sean Lip'


import numbers
import json


def List(val):
    """The given value should be a list."""
    try:
        if isinstance(val, str):
            val = json.loads(val)
        assert isinstance(val, list)
    except:
        return None
    return val


def NonnegativeInt(val):
    """The given value should be a non-negative integer."""
    try:
        val = int(val)
        assert val >= 0
    except:
        return None
    return val


def Number(val):
    """The given value should be a number."""
    try:
        val = float(val)
    except:
        return None
    return val


def Real(val):
    """The given value should be a real number."""
    try:
        val = float(val)
        assert isinstance(val, numbers.Real)
    except:
        return None
    return val


def Set(val):
    """The given value should be a list with unique elements."""
    try:
        if isinstance(val, str):
            val = json.loads(val)
        assert isinstance(val, list)
        assert len(set(val)) == len(val)
    except:
        return None
    return val


def String(x):
    """Collapses spaces and makes all characters of a string lowercase."""
    try:
        return ' '.join(unicode(x).lower().split())
    except:
        return None
