from collections.abc import Iterable
import collections
from collections import OrderedDict
from  itertools import filterfalse
import itertools
from operator import itemgetter



#  issue1:
def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return sum(1 for e in iterable)


# issue2:
def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """
    for elem in iterable:
        if isinstance(elem, collections.Iterable):
            yield from flatten(elem)
        else:
            yield elem


#issue3:
def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    seen = set()
    seen_add = seen.add
    for elem in filterfalse(seen.__contains__, iterable):
        seen_add(elem)
        yield elem


#issue4:
def groupby(key, iterable: Iterable):
    """
    # >>> users = [
        # {'gender': 'female', 'age': 33},
        # {'gender': 'male', 'age': 20},
        # {'gender': 'female', 'age': 21},
    # ]
    >>> users = [{'gender': 'female', 'age': 33}, {'gender': 'male', 'age': 20}, {'gender': 'female', 'age': 21},]
    >>> groupby('gender', users)
        {'female': [{'gender': 'female', 'age': 33}, {'gender': 'female', 'age': 21},],'male': [{'gender': 'male', 'age': 20}],}
    # >>> groupby('age', users)
    """
    result_dict = {}
    for elem in iterable:
        if elem[key] not in result_dict:
            result_dict[elem[key]]=list()
            result_dict[elem[key]].append(elem)
        else:
            result_dict[elem[key]].append(elem)
    return result_dict
