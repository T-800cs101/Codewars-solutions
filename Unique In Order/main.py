def unique_in_order(iterable):
    result = []
    j = 0
    for i in range(len(iterable)):
        if len(result) > 0:
            if iterable[i] != result[j]:
                result.append(iterable[i])
                j = j+1
        else:
            result.append(iterable[i])    
    return result
