## Q1

What is the reason why I get KeyError. The notebook 'Frequent_Patterns' works
fine but this assginment03 has an error, I assume this is as I'm not using
frozenset, but want to implement it without using fronzenset.

## A1

The KeyError occurs because of the different ways the patterns are stored in the
dictionaries:

1. In

Frequent_Patterns.ipynb

, patterns are stored using `frozenset` as keys:

```python
self.patterns[frozenset(pattern[:-1])] = pattern[-1]
```

2. In

assignment03.ipynb

, patterns appear to be stored as tuples:

```python
key = tuple(map(int, key.split(",")))
self.patterns[key] = int(value)
```

To fix this without using `frozenset`, you need to:

1. Either convert your subsets to tuples when generating them:

```python
# Change this line
subsets = []
for i in range(1, min(m, len(tran)) + 1):
    # Convert combinations to sorted tuples to ensure consistent ordering
    subsets.extend(tuple(sorted(c)) for c in combinations(tran, i))
```

2. Or modify how you store patterns in `__init__` to match your subset format:

```python
key = tuple(sorted(map(int, key.split(","))))  # Sort to ensure consistent ordering
self.patterns[key] = int(value)
```

The key is to use the same format (either tuples or frozensets) consistently
throughout the code when storing and looking up patterns.

## Q2

Then, what would be the reason why frozenset is used. What does frozenset do?

## A2

`frozenset` is used in this code for two key reasons:

1. **Immutability**:

- `frozenset` is an immutable version of `set`
- Once created, its elements cannot be modified
- This makes it suitable for use as dictionary keys, unlike regular `set`
  objects

2. **Hashability**:

- `frozenset` is hashable, meaning it can be used as a dictionary key
- In this code, patterns are stored as keys in dictionaries:

```python
self.patterns[frozenset(pattern[:-1])] = pattern[-1]
C = Counter()  # Counter is a dictionary subclass
```

Example:

```python
# This works - frozenset is hashable
patterns = {}
pattern = frozenset([1,2,3])
patterns[pattern] = 5

# This fails - set is not hashable
patterns = {}
pattern = set([1,2,3])
patterns[pattern] = 5  # TypeError: unhashable type: 'set'
```

For pattern mining, we need to:

1. Store patterns as sets (order doesn't matter)
2. Use these patterns as dictionary keys
3. Ensure patterns can't be modified accidentally

`frozenset` satisfies all these requirements, making it the ideal data structure
for this use case.

## Q3

so since I used tuple it's not hashable?

## A3

Actually, tuples ARE hashable - that's not the issue here. The error likely
occurs because:

1. In

assignment03.ipynb

you store patterns as tuples:

```python
key = tuple(map(int, key.split(",")))
self.patterns[key] = int(value)
```

2. But when generating subsets, you get different tuple orderings:

```python
subsets.extend(list(map(tuple, combinations(transaction, i))))
```

The issue is consistency in how elements are ordered. For example:

```python
# These are different tuples:
(1,2,3) != (2,1,3)

# But these are the same frozenset:
frozenset([1,2,3]) == frozenset([2,1,3])
```

To fix this without using frozenset, you need to ensure consistent ordering:

```python
# In subset generation:
subsets.extend(tuple(sorted(c)) for c in combinations(transaction, i))

# And in pattern loading:
key = tuple(sorted(map(int, key.split(","))))
```

`frozenset` handles this automatically, which is why it works in the reference
implementation. The issue isn't hashability (both tuples and frozensets are
hashable) but rather the order-independence of pattern matching.

## Q4

then is there any other data type that is more suitable than tuple and
frozenset?

## A4

For storing sets of items in pattern mining, `frozenset` and sorted `tuple` are
actually the most suitable data types. Here's why:

1. Requirements for pattern storage:

- Must be hashable (to use as dictionary keys)
- Must handle unordered collections
- Must be immutable
- Must be efficient for lookups

2. Available Python data types comparison:

|              | Mutable | Ordered | Hashable |
| ------------ | :-----: | :-----: | :------: |
| **List**     |    o    |    o    |    x     |
| **Set**      |    o    |    x    |    x     |
| **Tuple**    |    x    |    o    |    o     |
| **Frozenset**|    x    |    x    |    o     |

```python
# List - mutable, ordered, not hashable
patterns[1,2,3]  # Can't use as dict key

# Set - mutable, unordered, not hashable
patterns{1,2,3}  # Can't use as dict key

# Tuple - immutable, ordered, hashable
patterns[(1,2,3)]  # Works but order-sensitive

# Frozenset - immutable, unordered, hashable
patterns[frozenset([1,2,3])]  # Perfect for this use case
```

`frozenset` is the most natural choice because:

- Patterns are inherently unordered (ABC = BCA = CAB)
- Hash operations are O(1)
- Built specifically for this kind of use case
- No need to maintain sorted order manually

If not using `frozenset`, sorted `tuple` is the next best option, but requires
explicit sorting to maintain consistency.

There isn't really a better alternative in Python's built-in types for this
specific use case.
