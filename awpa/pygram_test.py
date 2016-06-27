import io

import pytest

from awpa.pgen2.driver import Driver
from awpa.pgen2 import tokenize
from awpa import pygram, pytree


@pytest.fixture(params=('py27', 'py33', 'py34', 'py35', 'pattern'))
def grammar_parts(request):
    return pygram.load_grammar(request.param)


@pytest.fixture
def driver(grammar_parts):
    token, grammar, symbols = grammar_parts
    return Driver(grammar, convert=pytree.convert)


def test_trivial_read(grammar_parts, driver):
    token, grammar, symbols = grammar_parts
    with io.open(token.__file__.rstrip('co'), encoding='utf-8') as infile:
        #tokenize.tokenize(token, infile.readline)
        s = infile.read()
    t = driver.parse_string(s)
    print(list(t.post_order()))
