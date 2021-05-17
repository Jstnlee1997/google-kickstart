def split(word):
    return [char for char in word]

T = int(input())
for test_case in range(T):
    S = split(input())
    ans = 0
    kcounter = 0
    if len(S) > 9:
        for i in range(len(S)-4):
            if S[i] == 'K' and S[i+1] == 'I' and S[i+2] == 'C' and S[i+3] == 'K':
                kcounter += 1
            elif S[i] == 'S' and S[i+1] == 'T'  and S[i+2] == 'A' and S[i+3] == 'R' and S[i+4] == 'T':
                ans += kcounter
    print("Case #{}: {} ".format(test_case+1, ans))
            
