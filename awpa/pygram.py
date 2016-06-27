# Copyright 2006 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.

"""Export the Python grammar and symbols."""

import importlib

import pkg_resources

from .pgen2 import driver, grammar


class Symbols(object):

    def __init__(self, grammar):
        """Initializer.

        Creates an attribute for each grammar symbol (nonterminal),
        whose value is the symbol's type (an int >= 256).
        """
        for name, symbol in grammar.symbol2number.items():
            setattr(self, name, symbol)


def load_grammar(which):
    token = importlib.import_module('awpa.gram_{}.token'.format(which))
    if not getattr(token, '_loaded', False):
        token.COMMENT, token.NL = 200, 201
        token.tok_name[200] = 'COMMENT'
        token.tok_name[201] = 'NL'
        token.opmap = grammar.make_opmap(token)
        token._loaded = True

    gram = driver.load_grammar(
        token,
        pkg_resources.resource_filename(token.__name__, 'Grammar.txt'))
    gram.token = token
    symbols = Symbols(gram)
    return token, gram, symbols
