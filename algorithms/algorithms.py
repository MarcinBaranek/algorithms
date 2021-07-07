import numpy as np


global bool_arr


def _permute(index, arr):
    global bool_arr
    n_elements = len(arr)
    for i in range(n_elements):
        if bool_arr[i] == 1:
            arr[index] = i
            bool_arr[i] = 0
            if index == n_elements - 1:
                yield arr
            else:
                yield from _permute(index + 1, arr)
            bool_arr[i] = 1


def permute(n_elements):
    """for a given natural number n_elements returns the generator of
    successive array permutations [0, 1, ..., n_elements - 1]"""
    global bool_arr
    bool_arr = [1 for _ in range(n_elements)]  # helpful array
    arr = np.arange(0, n_elements)  # array for permutation
    return _permute(0, arr)


def _select_switch(number, n_elements):
    counter = 0
    p = number
    while p % 2 == 0:
        p = p / 2
        counter += 1
    return n_elements - counter


def all_subsets(n_elements, empty=True):
    """for a given natural number n_elements returns the generator of
    successive array indicating which elements to include
    (indices with a value of 1) and which not (indices with a value of 0)"""
    if empty:
        yield np.zeros(n_elements)
    arr = np.zeros(n_elements)
    number = 1
    while number < 2**n_elements:
        index = _select_switch(number, n_elements)
        arr[index - 1] = 1 - arr[index - 1]  # negative
        yield arr
        number += 1


def all_k_elemental_subset(n, k):
    arr = np.arange(0, k)
    yield arr
    while arr[0] != n - k + 1:
        m = k - 1
        while arr[m] == n - k + m + 1:
            m = m - 1
        arr[m] = arr[m] + 1
        j = m + 1
        while j < k:
            arr[j] = arr[j - 1] + 1
            j = j + 1
        yield arr


def mesh_creator(*arrays):
    """returns the generator of all possible points in the
    Cartesian product *arrays"""
    if len(arrays) == 1:
        for element in arrays[0]:
            yield element
    else:
        for element in arrays[-1]:
            for others in mesh_creator(*arrays[:-1]):
                if len(arrays) > 2:
                    others.append(element)
                    yield others
                else:
                    yield [others, element]
