def zeros(n):
    sum = 0
    for i in range(1, n+1):
        while i % 5 == 0:
            sum += 1
            i = i // 5
    return sum

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
