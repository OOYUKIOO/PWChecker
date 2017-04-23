def pwChecker(pw):
    lower = [x for x in pw if x.islower()]
    upper = [x for x in pw if x.isupper()]
    nums = [x for x in pw if x.isdigit()]
    if len(lower)!=0 and len(upper)!=0 and len(nums)!=0:
        return True
    else:
        return False

def pwRate(pw):
    lower = [x for x in pw if x.islower()]
    upper = [x for x in pw if x.isupper()]
    nums = [x for x in pw if x.isdigit()]
    punc = [x for x in pw if x in ".?!&#,;:-_*"]
    rate = 0
    if len(pw)>=8:
        if len(nums)!=0:
            rate+=1
        if len(lower)!=0:
            rate+=2
        if len(upper)!=0:
            rate+=3
        if len(punc)!=0:
            rate+=4
    else:
        rate = 1
    return rate
    
