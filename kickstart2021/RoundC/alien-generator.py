T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    G = info1_split[0]
    n = 1
    ans = 0
    while G >= n*(n+1)/2:
            K = G/n
            if (K-(n-1)/2)-int(K-(n-1)/2) == 0:
                ans += 1
            n += 1

    print("Case #{}: {} ".format(test_case+1, ans))