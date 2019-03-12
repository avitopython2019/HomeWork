"""
>>> from morse import encode

>>> encode('HELLO')
'.... . .-.. .-.. ---'

>>> encode('SOS')
'... --- ...'


>>> encode()
Traceback (most recent call last):
...
TypeError:
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.IGNORE_EXCEPTION_DETAIL)
