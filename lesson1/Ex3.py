def zeros(n):
    sum = 0
    for i in range(5, n+1, 5):
        while i % 5 == 0:
            sum += 1
            i = i // 5
    return sum
