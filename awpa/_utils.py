import io

from .pgen2 import tokenize


def detect_future_features(grammar, source):
    token = grammar.token
    have_docstring = False
    gen = tokenize.generate_tokens(token, io.StringIO(source).readline)

    def advance():
        tok = next(gen)
        return tok[0], tok[1]

    ignore = frozenset((token.NEWLINE, token.NL, token.COMMENT))
    features = set()
    try:
        while True:
            tp, value = advance()
            if tp in ignore:
                continue
            elif tp == token.STRING:
                if have_docstring:
                    break
                have_docstring = True
            elif tp == token.NAME and value == 'from':
                tp, value = advance()
                if tp != token.NAME or value != '__future__':
                    break
                tp, value = advance()
                if tp != token.NAME or value != 'import':
                    break
                tp, value = advance()
                if tp == token.OP and value == '(':
                    tp, value = advance()
                while tp == token.NAME:
                    features.add(value)
                    tp, value = advance()
                    if tp != token.OP or value != ',':
                        break
                    tp, value = advance()
            else:
                break
    except StopIteration:
        pass
    return frozenset(features)


def decode_bytes_using_source_encoding(b):
    encoding = tokenize.detect_encoding(io.BytesIO(b).readline)[0]
    return b.decode(encoding)


def read_file_using_source_encoding(filename):
    with open(filename, 'rb') as infile:
        encoding = tokenize.detect_encoding(infile.readline)[0]
    with io.open(filename, 'r', encoding=encoding) as infile_with_encoding:
        return infile_with_encoding.read()
