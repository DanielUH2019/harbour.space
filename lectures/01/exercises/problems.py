"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations
from imaplib import ParseFlags


def normalize_username(name: str) -> str:
    """Return a normalized username.

    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    
    n = name.strip().lower().split()
    return "_".join(n)



def is_valid_age(age: int) -> bool:
    """Return True if age is in [18, 120], otherwise False."""
    return age >= 18 and age <= 120


def truthy_values(values: list[object]) -> list[object]:
    """Return a new list containing only truthy values from input."""
    return [v for v in values if v]


def sum_until_negative(numbers: list[int]) -> int:
    """Return sum of numbers until the first negative value (exclusive)."""
    x = 0
    for y in numbers:
        if y < 0:
            break 
        x+=y
    return x

def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    """Return numbers excluding values divisible by 3."""
    results = []
    for x in numbers:
        if x % 3 == 0:
            continue
        results.append(x)
    return results


def first_even_or_none(numbers: list[int]) -> int | None:
    """Return the first even number, or None if no even number exists."""
    for x in numbers:
        if x % 2 == 0:
            return x 
    return None


def squares_of_even(numbers: list[int]) -> list[int]:
    """Return squares of all even numbers in input order."""
    r = []
    for x in numbers:
        if x % 2 == 0:
            r.append(x**2)
    return r


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return dict mapping each word to its length."""
    r = {}
    for w in words: 
        r[w] = len(w)
    return r


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    return list(zip(keys, values))


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    """Build and return {'name': name, 'role': role, 'active': active}."""
    return {"name": name, "role": role, "active": active}


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    """Append tag to tags safely (no shared mutable default across calls)."""
    if not tags:
        tags = []
    tags.append(tag)
    return tags


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    """Invert mapping. Assume values are unique."""
    r = {}
    for k, v in zip(mapping.keys(), mapping.values()):
        r[v] = k
    return r


def unique_sorted_tags(tags: list[str]) -> list[str]:
    """Return unique tags sorted ascending."""
    return sorted(set(tags))


def count_words(words: list[str]) -> dict[str, int]:
    """Count occurrences of each word using collections.Counter."""
    from collections import Counter
    return Counter(words)


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    """Group scores by student name using collections.defaultdict(list)."""
    from collections import defaultdict
    a = defaultdict(list)
    for name, score in records:
        a[name].append(score)
    return a


def rotate_queue(items: list[str], steps: int) -> list[str]:
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    from collections import deque
    d = deque(items)
    d.rotate(steps)
    return list(d)


def safe_int(value: str) -> int | None:
    """Convert string to int, returning None if conversion fails."""
    try:
        return int(value)
    except:
        return None


def read_lines(path: str) -> list[str]:
    """Read a text file with a context manager and return non-empty stripped lines."""
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    """Return top `n` scores in descending order."""
    scores.sort(reverse=True)
    return scores[:n]

def all_passed(scores: list[int], threshold: int = 50) -> bool:
    """Return True if every score is >= threshold."""
    for v in scores:
        if v < threshold:
            return False
    return True
