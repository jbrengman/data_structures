
def sort(iterable):
    for i in range(1, len(iterable)):
        j = i - 1
        val = iterable[i]
        while val < iterable[j] and j >= 0:
            iterable[j+1] = iterable[j]
            j -= 1
        iterable[j+1] = val
    return iterable

if __name__ == '__main__':
    '''
    Compare average times of sorting for best and worst case lists of
    of 1,000,000 values.
    '''
    from time import time

    worst_avg = 0
    best_avg = 0

    worst = []
    for x in range(0, 1000000):
        worst.append(x)

    best = []
    for x in range(0, 1000000, -1):
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
    print('Average worst case sort time for 1,000,000 values: %s' % t_worst)
    print('Average best case sort time for 1,000,000 values: %s' % t_best)
