from itertools import combinations, permutations


s = 'XbanTanaY'

def bananas(s) -> set:
    lst = []
    comb =[]
    result = set()
    if len(s) > 6:
        m = s + ('-' * (len(s) - 6))
        n = set(combinations(m, len(s)))
        for i in n:
            if set('banana').issubset(i):
                lst.append(i)
        for t in lst:
            itertools.permutations(iterable, r=None)
    return comb