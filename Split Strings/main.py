def solution(s):
    s = list(s)
    str = ""
    result = []
    for i in range(0,len(s),2):
        if i+1 < len(s):
            str = s[i]+s[i+1]
        else:
            str = s[i]+'_'
        result.append(str)
    return result
        
