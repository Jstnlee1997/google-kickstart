T = int(input())
for test_case in range(T):
    N = int(input())
    A = list(map(lambda x: int(x), input().split()))
    ans = 0
    difference = 0
    count = 0
    for i in range(1,N):
        if count == 0:
            difference = A[i] - A[i-1]
            count += 1
        else:
            if A[i] - A[i-1] == difference:
                count += 1

            else:
                if count + 1 > ans:
                    ans = count + 1
                count = 1
                difference = A[i] - A[i-1]
        if i == N-1:
            if count + 1 > ans:
                ans = count + 1

    print("Case #{}: {} ".format(test_case+1, ans))