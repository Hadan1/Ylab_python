from itertools import combinations


def bananas(s) -> set:
    lst = []
    lenght = len(s) - 6
    comb = list(combinations(range(len(s)), lenght))
    for i in comb:
        word = list(s)
        for t in i:
            word[t] = '-'
        if (''.join(word)).replace('-','') == 'banana':
            lst.append(''.join(word))
    return set(lst)