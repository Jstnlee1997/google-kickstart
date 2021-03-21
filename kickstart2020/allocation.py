T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    N = info1_split[0]
    B = info1_split[1]
    A = list(map(lambda x: int(x), input().split()))
    A_sorted = sorted(A)
    ans = 0
    A_sum = 0
    for i in range(len(A_sorted)):
        if A_sum + A_sorted[i] <= B:
            A_sum += A_sorted[i]
            ans += 1
        else:
            break
    print("Case #{}: {} ".format(test_case+1, ans))