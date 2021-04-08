import math as mt

T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    N = info1_split[0]
    K = info1_split[1]
    M =  list(map(lambda x: int(x), input().split()))
    dict1 = {}
    start = M[1] - M[0]
    for i in range(1,N):
        diff = M[i] - M[i-1]
        if diff > start:
            start = diff
        dict1[diff] = 1
    ans = mt.ceil(start/2)
    for key in reversed(range(2,start+1)):
        if key in dict1.keys():
            if dict1[key] > K:
                ans = key
                break
            else:
                if key == 2:
                    ans = 1
                else:
                    K -= dict1[key]
                    new_key = mt.ceil(key/2)
                    dict1[new_key] = dict1[key]*2
                    del dict1[key]
    print("Case #{}: {} ".format(test_case+1, ans))