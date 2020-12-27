from collections import Counter
import math
def prime_factors(n):
    print(n)
    a = []
    result = []
    string = ""

    while n% 2 == 0:
        a.append(2)
        n /=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            a.append(i)
            n /=i
    if n > 2:
        a.append(int(n))
    print(a)
    b = Counter(a)
    b = sorted(b.items())
    a = set(a)
    result = list(a)
    result.sort()
    print(result)
    print(b)
    for i in range(len(result)):
        if result[i] == b[i][0]:
            if b[i][1] > 1:
                string += "("+str(result[i])+"**"+str(b[i][1])+")"
            else:
                string += "("+str(result[i])+")"
    if len(result) <= 1:
        string = "("+str(n)+")"
    return string
