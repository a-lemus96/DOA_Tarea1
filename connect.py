# standard library
import argparse
import random
from typing import Callable, List, Tuple

# config parser
parser = argparse.ArgumentParser()

parser.add_argument("-m", "--method", type=str,
                    choices=['qfind', 'qunion'], default='qfind',
                    help="Choose between quick-find or quick-union method")
parser.add_argument("-N", type=int, default=10,
                    help="Sets range of possible node values for random test")
parser.add_argument("-M", type=int, default=12,
                    help="Number of random input pairs for random test")

args = parser.parse_args()

def quick_find(
        A: List[int],
        p: int,
        q: int
        ) -> bool:
    r""""""
    x = A[p]
    y = A[q]
    # check if both elements are in different sets
    if x != y:
        # perform slow union
        for k in range(len(A)):
            if A[k] == x: A[k] = y
        return True

    return False

def quick_union(
        A: int,
        p: int,
        q: int
        ) -> bool:
    r""""""
    i = p
    # find root for p
    while A[i] != i:
       i = A[i]

    j = q
    # find root for q
    while A[j] != j:
        j = A[j]

    # check if both roots are the same or not
    if i != j:
        A[i] = j
        return True
    else:
        return False

def solve_connectivity(
        A: List[int],
        C: List[Tuple[int]],
        method: Callable) -> None:
    r""""""    
    count = 0 # counter for the number of connected components

    # iterate through all potential connections
    print("Input\t\tSets of connected nodes")
    for p, q in C:
        # call method for testing and potentially adding connection
        meaningful = method(A, p, q)
        if meaningful:
            print(f"*{p, q}\t\t{A}")
            count += 1
        else:
            print(f"-{p, q}\t\t{A}")

        # check if all nodes are connected
        if count >= len(A) - 1:
            print(f"\nGraph has already N - 1 connections. Stopping...")
            break

# use input from Sedgewick's book, section 1.2
C1 = [(3, 4),
      (4, 9),
      (8, 0),
      (2, 3),
      (5, 6),
      (2, 9),
      (5, 9),
      (7, 3),
      (4, 8),
      (5, 6),
      (0, 2),
      (6, 1)]

# generate M random input pairs between N possible node values
C2 = [tuple(random.sample(range(args.N), 2)) for m in range(args.M)]

# get method parameter from arguments
method = quick_find if args.method == 'qfind' else quick_union

# initialize list for the first test
A = list(range(10))
print(f"Initial sets of connected nodes:\n{A}\n")

# solve connectivity problem for the first input
solve_connectivity(A=A, C=C1, method=method)

# initialize list for the first test
A = list(range(args.N))
print(f"\nInitial sets of connected nodes:\n{A}\n")

# solve connectivity problem for random input
solve_connectivity(A=A, C=C2, method=method)

print("\n* denotes new connections")
print("- denotes redundant connections")
