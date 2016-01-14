__author__ = 'stephane'

def mean(sample):
    """
    computes the arithmetic mean of a sample
    :param sample: values to be averaged
    :return: arithmetic mean
    """
    tot = 0.0
    for elem in sample:
        tot += elem
    return tot/len(sample)

def median(sample):
    """
    computes the median of a sample
    :param sample: values to be averaged
    :return: median
    """
    # first, sort sample
    sample.sort()
    # if odd number of items
    if len(sample) % 2 != 0:
        return sample[len(sample)/2]
    else:
        n1 = sample[len(sample)/2-1]
        n2 = sample[len(sample)/2]
        return (n1 + n2) / 2.0

def mode(sample):
    """
    computes the mode of a sample
    i.e. the item occurring the most
    :param sample: values to be averaged
    :return: mode
    """
    # first sort sample
    sample.sort()
    # count occurrences
    max_nb = 0
    most_freq = 0
    current = 0
    nb = 0
    for elem in sample:
        if elem != current:
            if nb > max_nb:
                max_nb = nb
                most_freq = current
            current = elem
            nb = 1
        else:
            nb += 1
    return most_freq