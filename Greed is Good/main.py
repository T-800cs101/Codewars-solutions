from collections import Counter
def score(dice):
    print(dice)
    result = 0
    dublicate = Counter(dice)
    if 1 in dice:
        if dublicate[1] >= 3:
            result = result +1000+((dublicate[1]-3)*100)
        else:
            result = result +(dublicate[1]*100)
    if 2 in dice:
        if dublicate[2] >= 3:
            result = result+200

    if 3 in dice:
        if dublicate[3] >= 3:
            result = result+300

    if 4 in dice:
        if dublicate[4] >= 3:
            result = result+400

    if 5 in dice:
        if dublicate[5] >= 3:        
            result = result+500+((dublicate[5]-3)*50)
        else:      
            result = result+ (dublicate[5]*50)
    if 6 in dice:
        if dublicate[6] >= 3:        
            result = result+600
    return result
    # your code here
