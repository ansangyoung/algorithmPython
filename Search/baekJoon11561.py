import math
testCases = int(input())
#testCases = 4
for i in range(testCases):
    stepStones = int(input())
    #testStepStones = [1, 2, 100, 1000000]
    #stepStones = testStepStones[i]
    low = 0
    mid = 0
    # highMax: x*(x+1)/2 = stepStones
    high = int(math.sqrt(2*(stepStones+1)))

    while(high-low > 1):
        mid = (low+high)//2
        # compareCal: (mid*(mid+1))//2 + min(x)-1 < stepStones ? low = mid : high = mid
        compareCal = (mid*(mid+1))//2 + (mid+1)
        if (compareCal < stepStones):
            low = mid
        else:
            high = mid

    if ((high*(high+1))//2 + (high+1) <= stepStones):
        print(high+1)
    else:
        print(low+1)
    
