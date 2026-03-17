"""Lecture 01 practice problems.

Implement each function below so tests pass.
Rules:
- Do not change function names/signatures.
- Keep implementations pure unless the function explicitly needs I/O.
- Use only the Python standard library.
"""

from __future__ import annotations


def normalize_username(name: str) -> str:
    name= name.lower().strip()
    rr =name.split()
    m="_".join(rr)
    
    return m
    
    """Return a normalized username.
    Rules:
    - Trim outer whitespace
    - Lowercase everything
    - Replace internal whitespace runs with a single underscore
    """
    raise NotImplementedError


def is_valid_age(age: int) -> bool:
    a= age>=18
    b= age <= 120
    r = a and b
    return r
    """Return True if age is in [18, 120], otherwise False."""
    raise NotImplementedError


def truthy_values(values: list[object]) -> list[object]:
    a=[]
    for i in values:
        if i:
            a.append(i)
    return a
    """Return a new list containing only truthy values from input."""
    raise NotImplementedError


def sum_until_negative(numbers: list[int]) -> int:
    a=0
    for i in numbers:
        if i <0:
            break
        a+=i
    return a
    """Return sum of numbers until the first negative value (exclusive)."""
    raise NotImplementedError


def skip_multiples_of_three(numbers: list[int]) -> list[int]:
    a=[]
    for i in numbers:
        if i %3==0:
            continue
        a.append(i)
    return a
    """Return numbers excluding values divisible by 3."""
    raise NotImplementedError


def first_even_or_none(numbers: list[int]) -> int | None:
    for i in numbers:
        if i %2==0:
            return i
    return None
    """Return the first even number, or None if no even number exists."""
    raise NotImplementedError


def squares_of_even(numbers: list[int]) -> list[int]:
    a=[]
    for i in numbers:
        if i%2==0:
            b= i*i
            a.append(b)
    return a
    """Return squares of all even numbers in input order."""
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    d={}
    for i in words:
        l =len(i)
        d[i]=l
    return d
    """Return dict mapping each word to its length."""
    raise NotImplementedError


def zip_to_pairs(keys: list[str], values: list[int]) -> list[tuple[str, int]]:
    l=[]
    for k,v in zip(keys, values):
        r=(k,v)
        l.append(r)
    return l
    """Zip keys and values into list of pairs. Ignore extras in longer list."""
    raise NotImplementedError


def build_user(name: str, role: str = "student", active: bool = True) -> dict[str, object]:
    d = {
        "name": name,
        "role": role,
        "active": active
    }
    return d
    """Build and return {'name': name, 'role': role, 'active': active}."""
    raise NotImplementedError


def append_tag_safe(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags=[]
    tags.append(tag)
    
    return tags
    """Append tag to tags safely (no shared mutable default across calls)."""
    raise NotImplementedError


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    d = {}
    for k,v in mapping.items():
        d[v] = k
    return d
    """Invert mapping. Assume values are unique."""
    raise NotImplementedError


def unique_sorted_tags(tags: list[str]) -> list[str]:
    a=set(tags)
    r=sorted(a)
    return r
    """Return unique tags sorted ascending."""
    raise NotImplementedError


def count_words(words: list[str]) -> dict[str, int]:
    a = {}
    for i in words:
        if i in a:
            a[i] = a[i] + 1
        else:
            a[i] = 1
    return a
    """Count occurrences of each word using collections.Counter."""
    raise NotImplementedError


def group_scores(records: list[tuple[str, int]]) -> dict[str, list[int]]:
    d = {}
    for i,j in records:
        if i not in d:
            d[i]=[]
        d[i].append(j)
    return d
    """Group scores by student name using collections.defaultdict(list)."""
    raise NotImplementedError


def rotate_queue(items: list[str], steps: int) -> list[str]:
    if not items:
        return []
    
    n=len(items)
    m=steps%n
    i=n-m
    
    a=items[i:]
    b= items[:i]
    
    return a+b
    """Rotate queue to the right by `steps` using collections.deque and return as list."""
    raise NotImplementedError


def safe_int(value: str) -> int | None:
    try:
        r=int(value)
        return r
    except ValueError:
        return None
    """Convert string to int, returning None if conversion fails."""
    raise NotImplementedError


def read_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        data = f.read()
    
    result = []
    for line in data.split("\n"):
        clean_line = line.strip()
        if clean_line != "":
            result.append(clean_line)
            
    return result
    """Read a text file with a context manager and return non-empty stripped lines."""
    raise NotImplementedError


def top_n_scores(scores: list[int], n: int = 3) -> list[int]:
    a=sorted(scores, reverse=True)
    d=a[:n]
    return d
    """Return top `n` scores in descending order."""
    raise NotImplementedError


def all_passed(scores: list[int], threshold: int = 50) -> bool:
    for i in scores:
        if i<threshold:
            return False
    return True
    """Return True if every score is >= threshold."""
    raise NotImplementedError
