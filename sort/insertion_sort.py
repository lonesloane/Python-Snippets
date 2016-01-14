import unittest
import random


def insertion_sort(seq):

    for p in range(1, len(seq)):

        while p != 0 and seq[p] < seq[p-1]:
            seq[p], seq[p-1] = seq[p-1], seq[p]
            p -= 1

    return seq


def insertion_sort2(seq):

    for p in range(1, len(seq)):

        if seq[p] >= seq[p-1]:
            continue

        p_value = seq[p]

        while p != 0 and p_value < seq[p-1]:
            seq[p] = seq[p-1]
            p -= 1

        seq[p] = p_value

    return seq


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        seq = [random.randrange(0, 1000) for _ in range(1000)]
        self.assertEqual(insertion_sort(seq), sorted(seq))

    def test_insertion_sort2(self):
        seq = [random.randrange(0, 1000) for _ in range(1000)]
        self.assertEqual(insertion_sort2(seq), sorted(seq))

if __name__ == '__main__':
    unittest.main()
