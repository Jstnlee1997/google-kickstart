T = int(input())
for test_case in range(T):
    input1 = list(map(lambda x: int(x), input().split()))
    N = input1[0]
    K = input1[1]
    A = list(map(lambda x: int(x), input().split()))
    ans = 0
    counter = 0
    for integer in range(0,N):
        if A[integer] == K:
            counter = 1
        elif A[integer] == K-counter:
            if A[integer] == 1:
                ans += 1
                counter = 0
            else:
                counter += 1
        else:
            counter = 0


    print("Case #{}: {} ".format(test_case+1, ans))