testCases = int(input())
for i in range(testCases):
    stepStones = int(input())
    low = 0
    mid = 0
    # x*(x+1)/2 = stepStones /2
    high = (int)sqrt(2*stepStones)

    while(high - low > 1):
        mid = (low+high)/2
        tmp = (mid*(mid+1))/2 + mid + 1
        if (tmp < stepStones):
            low = mid
        else:
            high = mid

    if ((high*(high+1))/2 + high + 1 <= stepStones):
        print(high+1)
    else:
        print(low+1)
