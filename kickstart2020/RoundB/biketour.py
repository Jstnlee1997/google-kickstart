T = int(input())
for test_case in range(T):
    N = int(input())
    H = list(map(lambda x: int(x), input().split()))
    ans = 0
    for hill in range(1, N-1):
        if H[hill] > H[hill-1] and H[hill] > H[hill+1]:
            ans += 1
    print("Case #{}: {} ".format(test_case+1, ans))