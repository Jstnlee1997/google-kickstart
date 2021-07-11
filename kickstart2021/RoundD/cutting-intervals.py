import numpy as np
T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    N = info1_split[0]
    C = info1_split[1]
    ans = N
    dict1 = {}
    for i in range(N):
        interval = list(map(lambda x: int(x), input().split()))
        # do not bother with it if the difference is only 1
        if interval[1] - interval[0] > 1:
            # add integers within the interval into the dictionary
            for number in range(interval[0]+1,interval[1]):
                if number in dict1:
                    dict1[number] += 1
                else:
                    dict1[number] = 1

    cuts = 1
    while cuts <= C and len(dict1) > 0:
        ans += dict1[max(dict1)]
        del dict1[max(dict1)]
        cuts += 1

    print("Case #{}: {} ".format(test_case+1, int(ans)))