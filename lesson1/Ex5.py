def count_find_num(primesL, limit):
    base = 1
    lst = list()
    for i in primesL:
        base = base * i
        continue
    if base > limit:
        return []
    for t in primesL:
        my_comb = base
        while my_comb <= limit:
            lst.append(my_comb)
            my_comb = my_comb * t
    for m in lst:
        for n in primesL:
            if m * n <= limit:
                lst.append(m * n)
    result = set(lst)
    return [len(result), max(result)]
