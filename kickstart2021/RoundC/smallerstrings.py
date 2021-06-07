import math
def split(word):
    return [char for char in word]

T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    N = info1_split[0]
    K = info1_split[1]
    S = split(input())
    # for each character, count the number of possibilities it can form. 
    # and position matters
    # change base K to base 10
    ans = 0
    # only need to care about first half of string since it is palindrome
    H = math.ceil(N/2)
    for char in range(H):
        # add to answer the number of characters smaller than it, multiplied by its position
        ans += (ord(S[char])-96-1)* K**(H-char-1)
    # check if first char of 2nd half is strictly more, then + 1 
    # do the above only if length of string is more than 1
    if N > 1 and S[H] > S[H-1] and ord(S[H])-96 <= K:
        ans += 1
    print("Case #{}: {} ".format(test_case+1, ans))
        