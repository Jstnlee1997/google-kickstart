import numpy as np

T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    R = info1_split[0]
    C = info1_split[1]
    G = np.zeros((R,C))
    for r in range(R):
        G[r] = list(map(lambda x: int(x), input().split()))
    # print(G)
    total = 0
    for row in range(len(G)):
        for col in range(len(G[0])):
            if col + 1 < len(G[0]):
                difference = G[row][col] - G[row][col+1]
                if difference > 1:
                    total += abs(difference) -1
                    G[row][col+1] += difference -1
                elif difference < -1:
                    total += abs(difference) -1
                    G[row][col] += abs(difference) -1
            if row + 1 < len(G):
                difference = G[row][col] - G[row+1][col]
                if difference > 1:
                    total += abs(difference) -1
                    G[row+1][col] += difference -1
                elif difference < -1:
                    total += abs(difference) -1
                    G[row][col] += abs(difference) -1

    for row in reversed(range(len(G))):
        for col in reversed(range(len(G[0]))):
            if col -1 >= 0:
                difference = G[row][col] - G[row][col-1]
                if difference > 1:
                    total += abs(difference) -1
                    G[row][col-1] += difference - 1
                elif difference < - 1:
                    total += abs(difference) - 1
                    G[row][col] += abs(difference) - 1
            if row - 1 >= 0:
                difference = G[row][col] - G[row-1][col]
                if difference > 1:
                    total += abs(difference) -1
                    G[row-1][col] += difference -1
                elif difference < -1:
                    total += abs(difference) -1
                    G[row][col] += abs(difference) -1   
    
    # print(G)
    # print(int(total))

    print("Case #{}: {} ".format(test_case+1, int(total)))