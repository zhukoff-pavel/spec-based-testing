import pytest
import example.module as module
import re

from spec_based_testing import libsl_mocker


def test_bar_mock(libsl_mocker):
    libsl_mocker("/foo/bar.libsl")

    res = module.UsageExample().use_bar()

    assert 0 <= res <= 100 , res


def test_baz_mock(libsl_mocker):
    libsl_mocker("/foo/baz.libsl")
    res = module.UsageExample().use_baz()

    assert res == 6, res


def test_string_mock(libsl_mocker):
    libsl_mocker("/foo/string.libsl")

    res = module.UsageExample().use_string()

    assert re.match("[a-zA-Z0-9]{1,5}", res), res