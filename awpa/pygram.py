# Part of the awpa package: https://github.com/habnabit/awpa
# See LICENSE for copyright.

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


def ensure_token(token, name):
    if getattr(token, name, None) is not None:
        return
    new_val = token.N_TOKENS
    token.N_TOKENS += 1
    setattr(token, name, new_val)
    token.tok_name[new_val] = name


_DEFAULT_EQUIVALENCES = (
    ('atom_expr', 'power'),
)


def add_equivalence(syms, choices):
    for choice in choices:
        value = getattr(syms, choice, None)
        if value is not None:
            break
    else:
        return

    setattr(syms, '_or_'.join(choices), value)


def load_grammar(which, equivalences=_DEFAULT_EQUIVALENCES):
    token = importlib.import_module('awpa.gram_{}.token'.format(which))
    if not getattr(token, '_loaded', False):
        ensure_token(token, 'COMMENT')
        ensure_token(token, 'NL')
        token.opmap = grammar.make_opmap(token)
        token._loaded = True

    gram = driver.load_grammar(
        token,
        pkg_resources.resource_filename(token.__name__, 'Grammar.txt'))
    gram.token = token
    for attempted_start in ('file_input', 'Matcher'):
        if attempted_start not in gram.symbol2number:
            continue
        gram.start = gram.symbol2number[attempted_start]
        break
    else:
        raise RuntimeError('no start symbol found in', gram)
    symbols = gram.symbols = Symbols(gram)
    for equivalence in equivalences:
        add_equivalence(symbols, equivalence)
    return token, gram, symbols
