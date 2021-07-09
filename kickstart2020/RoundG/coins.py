import numpy as np

T = int(input())
for test_case in range(T):
    N = int(input())
    cells = np.zeros((N,N))
    for row in range(N):
        row_info = list(map(lambda x: int(x), input().split()))
        for col in range(N):
            cells[row][col] = row_info[col]

    # Total number of diagonals = (N-1)*2 + 1
    max_coins = 0
    # # iterate starting from top row first, starting at cell (1,1) followed by (1,2) ...
    for col in range(N):
        row = 0 # first row
        diagonal = cells[row][col]
        while row + 1 < N and col + 1 < N:
            row += 1
            col += 1
            diagonal += cells[row][col]
        if diagonal > max_coins:
            max_coins = diagonal
    
    # Next iterate through the first col
    for row in range(1,N):
        col = 0 # first col
        diagonal = cells[row][col]
        while row + 1 < N and col + 1 < N:
            row += 1
            col += 1
            diagonal += cells[row][col]
        if diagonal > max_coins:
            max_coins = diagonal
    
    print("Case #{}: {} ".format(test_case+1, int(max_coins)))