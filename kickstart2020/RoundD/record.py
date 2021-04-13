T = int(input())
for test_case in range(T):
    N = int(input())
    V = list(map(lambda x: int(x), input().split()))
    ans = 0
    high = V[0]

    # Check first element
    if V[0] > V[1]:
        ans +=1
    for i in range(1,N-1):
        if V[i] > high:
            high = V[i]
            if V[i] > V[i+1]:
                ans +=1

    # Check for last element
    if V[-1] > high:
        ans +=1

    print("Case #{}: {} ".format(test_case+1, ans))