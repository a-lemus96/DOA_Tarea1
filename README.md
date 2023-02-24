# Design of Algorithms - Assignment 1

This repository contains a Python implementation of the Merge Sort algorithm and two solutions to the connectivity problem formulated in section 1.2 of the book *Algorithms in C++* by R. Sedgewick.

## Merge Sort
The implementation is contained within `mergesort.py` and it is highly inspired in the pseudocodes from chapter 2 of the book *Introduction to Algorithms* by T. Cormen et. al.

### Program description
The program takes two arguments, `-N` which defines the range of possible values for the array to be sorted, that is `[0..N-1]`, and `-M` denoting the lenght of the array. These values are set to 20 by default, but can be changed arbitrarily by executing the script as follows:

`python mergesort.py -N=n -M=m`

being `n` and `m` the values of your preference.

There is no need to specify the array values as the program automatically generates random values depending on the hyperparameters you set. The program runs and displays two tests, it shows the array before and after the sorting in each case. Here is an execution of the script:

![image](https://user-images.githubusercontent.com/95151624/221078024-9462fa03-3308-49f9-9f86-0761a3ee7ec1.png)

## Connectivity Problem
Here we implement a Python version of the Quick-Find and Quick-Union solutions to the aforementioned connectivity problem. The solution is coded into `connect.py` and is highly inspired on the code proposed by R. Sedgewick.

### Program description
The program takes three arguments: `-m` or `--method` which can only take on the values {`qfind`, `qunion`} denoting the choice of one of the methods mentioned before (defaults to `qfind`), `-N` which serves the same purpose as in `mergesort.py`, and `-M` which denotes the number of input pairs.
To execute the program we run:

`python connect.py -m=(either qfind or qunion) -N=n -M=m`

again, being `n` and `m` the values of your preference.

Once you run the script, the program first solves the problem for the input case in Sedgewick's book and then it generates a random test case for the parameters `-N` and `M` you specified. Here is a run of the script for the quick-find solution, wich is the default method:

![image](https://user-images.githubusercontent.com/95151624/221082321-a33b904a-059d-42e9-80f5-a81442ae94e8.png)

And here is a testcase for the quick-union solution:

![image](https://user-images.githubusercontent.com/95151624/221082651-f32948ed-dd2e-4379-b719-be8bfec1ebad.png)

As you may have noticed, the program is able to stop once we reach `N-1` non-redundant connections.
