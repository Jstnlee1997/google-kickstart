from collections import deque
T = int(input())
for test_case in range(T):
    N = int(input())
    S = list(input())
    stack = deque()
    ans = []
    for i in range(N):
        if len(stack)>0:
            if S[i] > S[i-1]:
                stack.append(S[i])
                ans.append(len(stack))
            else:
                ans.append(1)
                stack = deque(S[i])
        else:
            stack.append(S[i])
            ans.append(len(stack))
    
    print("Case #{}: {} ".format(test_case+1, ' '.join(str(x) for x in ans)))