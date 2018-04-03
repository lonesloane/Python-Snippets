import unittest
import random


def merge_sort2(seq):
    if len(seq) <= 1:           # an array of length 1 is ordered, no need to split any further
        return seq

    mid = len(seq)//2           # prepare to split the problem in 2 halves
                                # // : explicit integer division
    return merge2(
        merge_sort2(seq[:mid]),  # 'divide' the problem in lesser order problems
        merge_sort2(seq[mid:]))  # and then, 'conquer' by merging the solutions of lesser order


def merge2(left, right):
    result = []
    left_ind, right_ind = 0, 0

    try:
        while True:
            while left[left_ind] < right[right_ind]:
                result.append(left[left_ind])
                left_ind += 1
            while right[right_ind] <= left[left_ind]:
                result.append(right[right_ind])
                right_ind += 1
    except IndexError:  # logic by exception is less efficient...
                        # and we will need to handle an exception at each recursion level !!!
        return result + right[right_ind:] + left[left_ind:]


def merge_sort(seq):

    if len(seq) <= 1:           # an array of length 1 is ordered, no need to split any further
        return seq

    mid = len(seq)//2           # prepare to split the problem in 2 halves
                                # // : explicit integrer division
    return merge(
        merge_sort(seq[:mid]),  # 'divide' the problem in lesser order problems
        merge_sort(seq[mid:]))  # and then, 'conquer' by merging the solutions of lesser order


def merge(left, right):
    result = []
    left_ind, right_ind = 0, 0
    left_len, right_len = len(left), len(right)

    while True:
        if left_ind < left_len:  # left not empty
            if right_ind < right_len:  # right not empty
                left_val = left[left_ind]
                right_val = right[right_ind]
                if left_val < right_val:
                    result.append(left_val)
                    left_ind += 1
                else:
                    result.append(right_val)
                    right_ind += 1
            else:  # right is empty, left is not empty
                return result + left[left_ind:]
        elif right_ind < right_len:  # left is empty, right is not empty
            return result + right[right_ind:]
        else:  # both are empty
            return result


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        seq = [random.randrange(0, 100000) for _ in range(100000)]
        self.assertEqual(merge_sort(seq), sorted(seq))

    def test_merge_sort2(self):
        seq = [random.randrange(0, 100000) for _ in range(100000)]
        self.assertEqual(merge_sort2(seq), sorted(seq))


if __name__ == '__main__':
    seq = [random.randrange(0, 1000) for _ in range(1000)]
    print(merge_sort2(seq))
#    unittest.main()