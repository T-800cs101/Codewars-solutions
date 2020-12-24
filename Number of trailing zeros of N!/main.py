def zeros(n):
    i = 5
    counter = 0
    while (n/i >= 1):
        counter += int(n/i)
        i *= 5
    return counter
