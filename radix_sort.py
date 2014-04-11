import Queue


def sort_int(it):
    result = []
    max_length = len(str(max(it)))
    place = 0
    que = Queue.Queue()
    for i in it:
        que.put(i)
    while place <= max_length:
        div = 10 ** place
        buckets = (
            {0: [], 1: [], 2: [], 3: [], 4: [],
                5: [], 6: [], 7: [], 8: [], 9: []})
        while not que.empty():
            i = que.get()
            if i // div == 0:
                result.append(i)
            else:
                buckets[(i // div) % 10].append(i)
        for x in range(10):
            for i in buckets[x]:
                que.put(i)
        place += 1
    return result


if __name__ == '__main__':
    '''
    Compare average sorting times for different cases of 100,000 value lists.
    These should all be relatively equal, because radix sort does not perform
    differently depending on the ordering of the input list.
    '''
    from time import time
    from random import randrange

    worst_avg = 0
    best_avg = 0
    rand_avg = 0

    worst = []
    for x in range(100000, 0, -1):
        worst.append(x)

    best = []
    for x in range(0, 100000):
        best.append(x)

    rand = []
    for x in range(0, 100000):
        rand.append(randrange(0, 100000))

    for x in range(10):
        w = worst
        start = time()
        sort_int(w)
        t_worst = time() - start
        worst_avg += t_worst

        b = best
        start = time()
        sort_int(b)
        t_best = time() - start
        best_avg += t_best

        r = rand
        start = time()
        sort_int(r)
        t_best = time() - start
        rand_avg += t_best

    worst_avg = str(worst_avg / 10)
    best_avg = str(best_avg / 10)
    rand_avg = str(rand_avg / 10)
    print(
        'Average sort time for 100,000 ascending presorted values: %s' %
        worst_avg)
    print(
        'Average sort time for 100,000 descending presorted values: %s' %
        best_avg)
    print('Average sort time for 100,000 random values: %s' % rand_avg)
