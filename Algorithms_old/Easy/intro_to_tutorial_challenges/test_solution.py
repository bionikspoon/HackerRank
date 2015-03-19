# coding=utf-8
import sys
from cStringIO import StringIO

import pytest

import solution


cases = []
case0_in = """
4
6
1 4 5 7 9 12
"""

case0_out = """
1
"""
cases.append((case0_in, case0_out))


@pytest.fixture(params=cases)
def case(request):
    return request.param


# noinspection PyShadowingNames
def test_cases(case, capsys):
    actual, expected = map(str.lstrip, case)
    sys.stdin = StringIO(actual)
    solution.main()
    out, _ = capsys.readouterr()
    sys.stdin = sys.__stdin__

    assert out == expected
