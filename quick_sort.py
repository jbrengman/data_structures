import insertion_sort


def sort(it):
    if len(it) <= 1:
        return it
    pivot = it.pop(0)
    less, greater = [], []
    for x in it:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)
    return sort(less) + [pivot] + sort(greater)


def quicker_sort(it):
    if len(it) < 10:
        return insertion_sort.sort(it)
    pivot = it.pop(get_pivot(it))
    less, greater = [], []
    for x in it:
        if x < pivot:
            less.append(x)
        else:
            greater.append(x)
    return sort(less) + [pivot] + sort(greater)


def get_pivot(it):
    indices = [0, len(it) - 1, (len(it) - 1) // 2]
    vals = [it[indices[0]], it[indices[1]], it[indices[2]]]
    max_ = max(vals)
    min_ = min(vals)
    for x in range(3):
        if vals[x] != max_ and vals[x] != min_:
            return indices[x]
    return 0


if __name__ == '__main__':
    '''
    Compare average times of sorting for best and worst case lists of
    of 1,000,000 values.
    '''
    from time import time
    from random import randrange
    from sys import setrecursionlimit
    setrecursionlimit(50000)

    avg_1 = 0
    avg_worst_1 = 0
    avg_2 = 0
    avg_worst_2 = 0

    for x in range(5):

        to_sort = []
        to_sort_worst = []

        for x in range(0, 10000):
            to_sort.append(randrange(100000))
            to_sort_worst.append(x)

        start = time()
        sort(to_sort)
        end = time() - start
        avg_1 += end

        start = time()
        sort(to_sort_worst)
        end = time() - start
        avg_worst_1 += end

        start = time()
        quicker_sort(to_sort)
        end = time() - start
        avg_2 += end

        start = time()
        quicker_sort(to_sort_worst)
        end = time() - start
        avg_worst_2 += end

    avg_1 = str(avg_1 / 5)
    avg_worst_1 = str(avg_worst_1 / 5)
    avg_2 = str(avg_2 / 5)
    avg_worst_2 = str(avg_worst_2 / 5)

    print('Average random list sort time for quick sort: %s' % avg_1)
    print('Average random list sort time for quicker sort: %s' % avg_2)
    print('Average worst case sort time for quick sort: %s' % avg_worst_1)
    print('Average worst case sort time for quicker sort: %s' % avg_worst_2)
