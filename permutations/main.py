import itertools
def permutations(string):
    result = [''.join(p) for p in itertools.permutations(string)]
    return set(result)
