"""
>>> from morse import *

>>> encode("AVITO")
'.- ...- .. - ---'

>>> encode("SOS")
'... --- ...'

>>> encode("!")
Traceback (most recent call last):
...
KeyError: Symbol wasn't found in LETTER_TO_MORSE
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
