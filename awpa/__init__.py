# Part of the awpa package: https://github.com/pyga/awpa
# See LICENSE for copyright.

from .pygram import load_grammar
from ._utils import (
    decode_bytes_using_source_encoding, read_file_using_source_encoding)
from ._version import get_versions


__version__ = get_versions()['version']
del get_versions


__all__ = (
    'load_grammar',
    'decode_bytes_using_source_encoding',
    'read_file_using_source_encoding',
    '__version__',
)
