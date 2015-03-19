# coding=utf-8
import sys
from cStringIO import StringIO

import pytest

import solution


cases = []
case0_in = """
5
2 4 6 8 3
"""

case0_out = """
2 4 6 8 8
2 4 6 6 8
2 4 4 6 8
2 3 4 6 8
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
