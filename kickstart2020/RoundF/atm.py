import math as mt
from operator import itemgetter
T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    N = info1_split[0]
    X = info1_split[1]
    A = list(map(lambda x: int(x), input().split()))
    for i in range(N):
        A[i] = [i,mt.ceil(A[i]/X)]
    A = sorted(A,key=itemgetter(1))
    print("Case #{}: {} ".format(test_case+1, ' '.join(str(x[0]+1) for x in A)))
