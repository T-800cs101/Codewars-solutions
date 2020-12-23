import collections

def find_uniq(arr):
    # your code here
    arr_1 = []
    result = 0
    arr_1 =([item for item, count in collections.Counter(arr).items() if count > 1])
    n = set(arr)
    for i in arr_1:
        if i in n:
            n.remove(i)
            n = list(n)
            n = n[0]
    return n   # n: unique integer in the array
