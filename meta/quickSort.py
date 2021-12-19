#!/bin/python

def quick_sort(ar):
    if len(ar) < 2:
        return ar
    lt, eq, rt = [], [], []
    for item in ar:
        if item < ar[0]:
            lt.append(item)
        elif item > ar[0]:
            rt.append(item)
        else:
            eq.append(item)
    sub = quick_sort(lt) + eq + quick_sort(rt)
    print(' '.join([str(x) for x in sub]))
    return(sub)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar)