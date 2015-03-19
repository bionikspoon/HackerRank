# coding=utf-8
import sys
from cStringIO import StringIO

import pytest

import solution


cases = []
case0_in = """
5
4 5 3 7 2
"""

case0_out = """
3 2 4 5 7
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
