### Debugging Exercise 1: Indexing a Set in Python

# Identified Issue

The original implementation attempted to retrieve an element by index from a Set.

However, in Python:

- A Set is an **unordered collection
- It does not support indexing
- Its iteration order is not guaranteed or deterministic

Because indexing relies on order, the returned results were unpredictable.

---

# Root Cause

The bug was not in the loop itself, but in the choice of data structure. Using a loop was merely a workaround to simulate indexing, since sets cannot be accessed by position. This represents a "design flaw", not a "syntax error".

---

# Correct Approach

Index-based access requires an ordered collection, such as a List.

# Overall Insight

- The original loop was necessary because sets are not indexable.
- However, the real issue was the incorrect data structure selection.
- Since indexing requires order, a list is the appropriate structure.

--- --- ---
--- --- ---
--- --- ---

### Debugging Exercise 2: Swapping Coordinates with NumPy

# Issue 1 – Obvious Error

The original assignment contained a typo:

```python
coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3] = \
coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]
```

Column `1` was duplicated on the right-hand side, which made the swap incorrect.

---

# Issue 2 – Deeper Problem (Memory Semantics)

Even after correcting the typo, the implementation remained flawed, since NumPy slicing returns views, not copies, which means:

- `coords[:, 0]` does not create a new array
- It references the same underlying memory
- In-place reassignment causes unintended overwriting

This results in corrupted swaps due to shared memory references.
This is a classic in-place mutation issue in vectorized numerical computing.

---

# Overall Insight

- The first issue was a typo in column reassignment.
- The deeper issue was misunderstanding NumPy's memory model.
- Since slicing returns views, in-place swaps can overwrite source data.
- The correct solution is to operate on a copy or use safe advanced indexing.
