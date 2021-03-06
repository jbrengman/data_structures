
'''
Idea for using left[i] and right[j] rather
than left.pop(0) and right.pop(0) taken from
http://stackoverflow.com/questions/18761766/mergesort-python
'''


def sort(iterable):
    if len(iterable) < 2:
        return iterable
    result = []
    mid = len(iterable) // 2
    left, right = sort(iterable[:mid]), sort(iterable[mid:])
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == '__main__':
    '''
    Compare average times of sorting for best and worst case lists of
    of 1,000,000 values.
    '''
    from time import time

    worst_avg = 0
    best_avg = 0

    worst = []
    for x in range(100000, 0, -1):
        worst.append(x)

    best = []
    for x in range(0, 100000):
        best.append(x)

    for x in range(10):
        w = worst
        start = time()
        sort(w)
        t_worst = time() - start
        worst_avg += t_worst

        b = best
        start = time()
        sort(b)
        t_best = time() - start
        best_avg += t_best

    worst_avg = str(worst_avg / 10)
    best_avg = str(best_avg / 10)
    print('Average worst case sort time for 100,000 values: %s' % worst_avg)
    print('Average best case sort time for 100,000 values: %s' % best_avg)
