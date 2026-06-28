
# Quicksort Implementation

import time, random, sys
sys.setrecursionlimit(300_000)

def quicksort_fixed(items, low=0, high=None):
    if high is None:
        high = len(items) - 1
    if low < high:
        split_at = settle_pivot(items, low, high)
        quicksort_fixed(items, low, split_at - 1)
        quicksort_fixed(items, split_at + 1, high)


def settle_pivot(items, low, high):
 
    anchor   = items[high]
    boundary = low - 1          
    for cursor in range(low, high):
        if items[cursor] <= anchor:
            boundary += 1
            items[boundary], items[cursor] = items[cursor], items[boundary]
    items[boundary + 1], items[high] = items[high], items[boundary + 1]
    return boundary + 1

# Randomized Quicksort

def quicksort_random(items, low=0, high=None):
    if high is None:
        high = len(items) - 1
    if low < high:
        split_at = settle_pivot_random(items, low, high)
        quicksort_random(items, low, split_at - 1)
        quicksort_random(items, split_at + 1, high)


def settle_pivot_random(items, low, high):
    draw = random.randint(low, high)
    items[draw], items[high] = items[high], items[draw]
    return settle_pivot(items, low, high) 


# Measurement Setup

def time_one_run(sort_fn, source):
    """Run sort_fn on a clone of source; return elapsed milliseconds."""
    clone = list(source)
    begin = time.perf_counter()
    sort_fn(clone)
    return (time.perf_counter() - begin) * 1000.0


def gen_shuffled(n):  return random.sample(range(n * 7), n)
def gen_sorted(n):    return list(range(n))
def gen_rev_sorted(n): return list(range(n, 0, -1))

input_kinds = [
    ('Shuffled',       gen_shuffled),
    ('Already Sorted', gen_sorted),
    ('Reverse Sorted', gen_rev_sorted),
]

sizes_to_test = [500, 1_000, 3_000, 10_000, 30_000]

print(f"{'Input':<16} {'n':>7}  {'Fixed (ms)':>11}  {'Random (ms)':>12}")
print('-' * 52)

for label, gen in input_kinds:
    for n in sizes_to_test:
        sample = gen(n)
        rand_ms = time_one_run(quicksort_random, sample)
        if label != 'Shuffled' and n > 3_000:
            fixed_label = '   overflow'
        else:
            fixed_ms    = time_one_run(quicksort_fixed, sample)
            fixed_label = f'{fixed_ms:>11.2f}'
        print(f"{label:<16} {n:>7}  {fixed_label}  {rand_ms:>12.2f}")
