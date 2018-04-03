import itertools


def power_set(sequence):
    for size in range(len(sequence) + 1):
        for item in itertools.combinations(sequence, size):
            yield item


def power_set_from(sequence):
    for size in range(len(sequence) + 1):
        yield from itertools.combinations(sequence, size)


for result in power_set('abc'):
    print(result)

for result in power_set_from('def'):
    print(result)
