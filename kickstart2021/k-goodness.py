def split(word):
    return [char for char in word]

T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    N = info1_split[0]
    K = info1_split[1]
    S = split(input())
    score = 0
    for i in range(1,int(N/2)+1):
        if S[i-1] != S[N-i]:
            score += 1
    ans = 0
    if score < K:
        ans = K - score
    print("Case #{}: {} ".format(test_case+1, ans))