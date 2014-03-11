This repository contains data structure implementations in Python and corresponding unit tests.



Linked List methods:

    insert()

    pop()

    size()

    search(value)

    remove(node)

    remove_by_value(value)

    contains(value)



Stack methods:

    push(value)

    pop()

    size()


Queue is implemented as a doubly linked list.

Queue methods:

    enqueue(value)

    dequeue()

    size()


Hash Table methods:

    set(key, value)

    get(key)

    hash(key)

hash_month.py: This is a subclass of hash_table

    make_month(year, month) - returns a hash_month object for the given month

    day(n) - returns the first two letters of the day of the week (ex: Mo, Tu, We, etc) for 
    he 'n'th day of the month.


Binary Search Tree (bst.py) methods:

    insert(value)

    contains(value)

    size()

    depth()

    balance()

    save_dot(): Saves a dot file for visualizing the tree.


[![Build Status](https://travis-ci.org/jbrengman/data_structures.png?branch=master)](https://travis-ci.org/jbrengman/data_structures)