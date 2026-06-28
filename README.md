# Assignment 5: Quicksort — Implementation, Analysis, and Randomization
**Dinesh Reddy Singireddy — University of the Cumberlands**

## Contents
- Deterministic Quicksort (fixed last-element pivot)
- Randomized Quicksort (uniformly random pivot)
- Timing harness comparing both across shuffled, sorted, and reverse-sorted data

## How to Run
python assignment5.py

## Key Findings
- Fixed-pivot Quicksort degrades to O(n²) on sorted/reverse-sorted input and crashes via recursion overflow above ~3,000 elements
- Randomized Quicksort stays O(n log n) regardless of input order
- On shuffled data both versions perform similarly
