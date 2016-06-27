import io

from awpa.pgen2 import driver, tokenize
from awpa import pygram, pytree


for v in 'py27 py33 py34 py35 pattern'.split():
    print(v)
    token, grammar, symbols = pygram.load_grammar(v)
    d = driver.Driver(grammar, convert=pytree.convert)
    with io.open(v + '.py', encoding='utf-8') as infile:
        #tokenize.tokenize(token, infile.readline)
        s = infile.read()
    t = d.parse_string(s)
    import pprint
    pprint.pprint(list(t.post_order()))
