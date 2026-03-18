"""Lecture 03 practice problems.

Implement each class/function below so tests pass.
Rules:
- Do not change names/signatures.
- Use only the Python standard library.

Problems:
1. Countdown iterator
2. Step iterator
3. Unique consecutive iterator
4. Circular iterator
6. File word reader generator
7. Batch generator
8. Recursive flatten generator (optional)
9. log_calls decorator
10. measure_time decorator
11. count_calls decorator
12. ensure_non_negative decorator
13. retry decorator (optional)
14. lru_cache decorator (optional)
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import Any


class Countdown:
    """Problem 1. Countdown iterator.

    Build an iterator class that starts at `n` and yields down to `0` inclusive.

    Example:
    >>> list(Countdown(3))
    [3, 2, 1, 0]
    """

    def __init__(self, n: int) -> None:
        self.current = n

    def __iter__(self) -> Iterator[int]:
        return self
    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration()
        value = self.current
        self.current -= 1
        return value

class StepIterator:
    """Problem 2. Step iterator.

    Iterate through a list by taking every `step`-th element.
    Default `step` is `2`.
    Raise `ValueError` when `step <= 0`.

    Example:
    >>> list(StepIterator([10, 20, 30, 40, 50, 60]))
    [10, 30, 50]
    >>> list(StepIterator([1, 2, 3, 4, 5, 6, 7], step=3))
    [1, 4, 7]
    """

    def __init__(self, values: list[Any], step: int = 2) -> None:
        if step <= 0:
            raise ValueError()
        self.values = values
        self.current = 0
        self.step = step
        

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.current >= len(self.values):
            raise StopIteration()
        
        value = self.values[self.current]
        self.current += self.step
        return value


class UniqueConsecutiveIterator:
    """Problem 3. Unique consecutive iterator.

    Yield values while removing only *consecutive* duplicates.

    Example:
    >>> list(UniqueConsecutiveIterator([1, 1, 2, 2, 2, 3, 1, 1]))
    [1, 2, 3, 1]
    """

    def __init__(self, values: list[Any]) -> None:
        self.current = 0
        self.values = values
        self.last_returned = None

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.current >= len(self.values):
            raise StopIteration()
        
        v = None 
        while self.last_returned == self.values[self.current]:
            self.current += 1
            if self.current == len(self.values):
                raise StopIteration()
            
        
        v = self.values[self.current]
        self.last_returned = v
        self.current += 1
        return v




class CircularIterator:
    """Problem 4. Circular iterator.

    Return exactly `k` values by cycling through `sequence`.
    Raise `ValueError` when sequence is empty or when `k < 0`.

    Example:
    >>> list(CircularIterator(["A", "B", "C"], 8))
    ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
    """

    def __init__(self, sequence: Sequence[Any], k: int) -> None:
        if len(sequence) == 0 or k < 0:
            raise ValueError()

        self.sequence = sequence
        self.k = k
        self.current = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.k == 0:
            raise StopIteration()

        if self.current == len(self.sequence):
            self.current = 0
        
        v = self.sequence[self.current]
        self.current += 1 
        self.k -= 1
        return v


class FlattenIterator:
    """Problem 5 (optional). Flatten iterator.

    Build an iterator class that yields scalar values from nested lists
    of arbitrary depth.

    Example:
    >>> list(FlattenIterator([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """

    def __init__(self, data: list[Any]) -> None:
        self.data = data
        self.current = 0

    def __iter__(self) -> Iterator[Any]:
        return self

    def __next__(self) -> Any:
        if self.current >= len(self.data):
            raise StopIteration()

        v = self.data[self.current]
        while not isinstance(v, int):
            self.current += 1
            if self.current == len(self.data):
                raise StopIteration()
            v = self.data[self.current]

        self.current += 1
        return v


def read_words(filename: str) -> Iterator[str]:
    """Problem 6. File word reader generator.

    Yield one word at a time from a text file without loading the whole
    file into memory.

    Example:
    >>> list(read_words("sample.txt"))
    ['one', 'two', 'three']
    """
    with open(filename, "r") as f:
        line = f.readline()
        while line :
            values = line.split()
            yield from values
            line = f.readline()


def batch(iterable: Iterable[Any], size: int) -> Iterator[list[Any]]:
    """Problem 7. Batch generator.

    Yield lists containing at most `size` items from `iterable`.
    Raise `ValueError` when `size <= 0`.

    Example:
    >>> list(batch([1, 2, 3, 4, 5, 6, 7], 3))
    [[1, 2, 3], [4, 5, 6], [7]]
    """
    if size <= 0:
        raise ValueError()
    
    r = []
    for i, x in enumerate(iterable):
        r.append(x)
        if len(r) == size:
            yield r
            r = []
    
    yield r



def flatten(data: list[Any]) -> Iterator[Any]:
    """Problem 8 (optional). Recursive flatten generator.

    Recursively yield all scalar values from a nested list.

    Example:
    >>> list(flatten([1, [2, 3], [4, [5, 6]], 7]))
    [1, 2, 3, 4, 5, 6, 7]
    """
    for x in data:
        if isinstance(x, int):
            yield x 
        else:
            yield from flatten(x)


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 9. `log_calls` decorator.

    Print each function call in this format:
    `name(arg1, arg2, kw=value) -> result`

    Hint:
    - Function name: `func.__name__`
    - Positional values: `args`
    - Keyword names/values: `kwargs.items()`

    Example:
    >>> @log_calls
    ... def add(a, b):
    ...     return a + b
    >>> add(2, 3)
    add(2, 3) -> 5
    5
    """
    raise NotImplementedError


def measure_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 10. `measure_time` decorator.

    Measure function execution time and print:
    `Executed in <milliseconds> ms`

    Example:
    >>> @measure_time
    ... def work():
    ...     return "done"
    >>> work()
    done
    """
    raise NotImplementedError


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 11. `count_calls` decorator.

    Count how many times the wrapped function is called.
    Store the counter in `wrapper.calls`.

    Example:
    >>> @count_calls
    ... def ping():
    ...     return "ok"
    >>> ping(); ping()
    'ok'
    >>> ping.calls
    2
    """
    raise NotImplementedError


def ensure_non_negative(func: Callable[..., Any]) -> Callable[..., Any]:
    """Problem 12. `ensure_non_negative` decorator.

    Raise `ValueError` when the decorated function returns a negative number.

    Example:
    >>> @ensure_non_negative
    ... def diff(a, b):
    ...     return a - b
    >>> diff(5, 2)
    3
    """
    raise NotImplementedError


def retry(times: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 13 (optional). `retry(times)` decorator.

    Retry a function up to `times` retries after the initial attempt.
    Raise `ValueError` when `times < 0`.

    Example:
    >>> @retry(2)
    ... def flaky():
    ...     ...
    """
    raise NotImplementedError


def lru_cache(maxsize: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Problem 14 (optional). `lru_cache(maxsize)` decorator factory.

    Implement cache with Least Recently Used eviction policy.
    Keep only the last `maxsize` used results.
    Solve this one using a class.

    Example:
    >>> @lru_cache(2)
    ... def square(x):
    ...     return x * x
    >>> square(2), square(3), square(2)
    (4, 9, 4)
    """
    raise NotImplementedError
