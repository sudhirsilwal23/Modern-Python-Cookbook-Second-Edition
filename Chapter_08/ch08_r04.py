"""Python Cookbook 2nd ed.

Chapter 8, recipe 4, Managing global and singleton objects
"""

import collections
from typing import List, Tuple, Any, Counter

_global_counter: Counter[str] = collections.Counter()


def count(key: str, increment: int = 1) -> None:
    _global_counter[key] += increment


def counts() -> List[Tuple[Any, int]]:
    return _global_counter.most_common()


class EventCounter:
    _counts: Counter[str] = collections.Counter()

    def count(self, key: str, increment: int = 1) -> None:
        EventCounter._counts[key] += increment

    def counts(self) -> List[Tuple[Any, int]]:
        return EventCounter._counts.most_common()


test_module_global = """
>>> from Chapter_08.ch08_r04 import *
>>> from Chapter_08.ch08_r03 import Dice1
>>> d = Dice1(1)
>>> for _ in range(1000):
...     if sum(d.roll()) == 7: count('seven')
...     else: count('other')
>>> print(counts())
[('other', 833), ('seven', 167)]
"""

test_class_variable = """
>>> from Chapter_08.ch08_r04 import *
>>> c1 = EventCounter()
>>> c1.count('input')
>>> c2 = EventCounter()
>>> c2.count('input')
>>> c3 = EventCounter()
>>> c3.counts()
[('input', 2)]
"""

__test__ = {n: v for n, v in locals().items() if n.startswith("test_")}
