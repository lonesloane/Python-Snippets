__author__ = 'stephane'

import unittest
import random


def partition(array, begin, end):
    pivot = begin
#    pivot = random.randint(0, len(array)-1)
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort_inplace(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin  >= end:
        return
    pivot = partition(array, begin, end)
    quick_sort_inplace(array, begin, pivot-1)
    quick_sort_inplace(array, pivot+1, end)


def quick_sort2(array):
    if not array:
        return []

    pivot = array[random.randint(0, len(array)-1)]
    return quick_sort2([x for x in array if x < pivot]) \
           + [x for x in array if x == pivot] \
           + quick_sort2([x for x in array if x > pivot])


def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[random.randint(0, len(array)-1)]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        seq = [random.randrange(0, 100000) for _ in range(100000)]
        self.assertEqual(quick_sort(seq), sorted(seq))

    def test_quick_sort2(self):
        seq = [random.randrange(0, 100000) for _ in range(100000)]
        self.assertEqual(quick_sort2(seq), sorted(seq))

    def test_quick_sort_inplace(self):
        seq = [random.randrange(0, 100000) for _ in range(100000)]
        quick_sort_inplace(seq)
        self.assertEqual(seq, sorted(seq))


if __name__ == '__main__':
    seq = [random.randrange(0, 1000) for _ in range(1000)]
    print quick_sort(seq)
#    unittest.main()