def zeros(n):
    result = 0
    while n > 0:
        n = n // 5
        result = n + result
    return result
