# Standard library
import argparse
from typing import List
import random

# config parser
parser = argparse.ArgumentParser()

parser.add_argument("-N", type=int, default=20,
                    help="Defines interval of possible values [0..N - 1]")
parser.add_argument("-M", type=int, default=20,
                    help="Size of array")

args = parser.parse_args()

def merge_sentinel(
        A: List[int],
        p: int,
        q: int,
        r: int) -> None:
    r""""""
    L, R = [], [] # left and right subarrays

    # set L to  A[p..q]
    for item in A[p:q + 1]:
        L.append(item)

    # set R to A[q+1:r]
    for item in A[q + 1: r + 1]:
        R.append(item) 

    # append sentinel values
    L.append(float('inf'))
    R.append(float('inf'))

    # initialize indexes
    i, j = 0, 0

    # merge subarrays
    for k in range(p, r + 1):
        if L[i] <= R[j]: # compare the two left-most elements in each subarray
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(
        A: List[int], 
        p: int, 
        r: int
        ) -> None:
    r""""""
    if p < r:
        q = (p + r) // 2 # partition A[p..r] into two subarrays
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge_sentinel(A, p, q, r)

# test for the first array
A1 = random.sample(range(0, args.N), args.M)
print(f"Array to sort:\n{A1}")
merge_sort(A1, 0, len(A1) - 1)
print(f"Array after sorting:\n{A1}")

# test for the second array
A2 = random.sample(range(0, args.N), args.M)
print(f"\nArray to sort:\n{A2}")
merge_sort(A2, 0, len(A2) - 1)
print(f"Array after sorting:\n{A2}")
