def bowling_score(frames):
    result = 0
    j = 1
    new_f = []
    f = frames.split()
    print(f)
    if all(item == f[0] for item in f[0:9])  and f[len(f)-1] == 'XXX':
        result = 300
    else:
        for i in range(len(f)):
            if i < len(f)-1:
                if '/' in f[i] and 'X' in f[i+1] and len(f[i+1]) != 3:
                    result += 20
                elif '/' in f[i] and '/' in f[i+1]:
                    result += 10 + int(f[i+1][0])
                elif '/' in f[i] and 'X' in f[i+1]:
                    result += 20
                
                elif '/' in f[i]:
                    result += 10 +int(f[i+1][0])
                elif 'X' in f[i]:
                    j = i
                    count = 0
                    while f[j] == 'X' and j<9:
                        result += 10
                        j += 1
                        count += 1
                    if count > 2:
                        print('more then 2 X')
                    if count == 2:
                        if f[j][0] != 'X':
                            result += int(f[j][0])
                        else:
                            result += 10
                    if count == 1:
                        if '/' in f[j]:
                            result += 10
                        elif j == 9:
                            if f[j][0] == 'X' and f[j][1] == 'X':
                                result +=  20
                            elif f[j][0] == 'X' or f[j][1] == '/':
                                result +=  10
                            else:
                                result += int(f[j][0])+ int(f[j][1])
                        else:
                            result += int(f[j][0])+ int(f[j][1])
                else:
                    result += int(f[i][0]) + int(f[i][1])
            else:
                if f[i] == 'XXX':
                    result += 30
                elif '/' in f[i]:
                    if f[i][2] != 'X':
                        result += 10 + int(f[i][2])
                    else:
                        result += 20
                else:
                    for a in range(len(f[i])):
                        if f[i][a] == 'X':
                            result += 10
                        else:
                            result += int(f[i][a])
    return result
