import numpy as np

T = int(input())
for test_case in range(T):
    G = []
    ans = 0
    first_row = list(map(lambda x: int(x), input().split()))
    # determine if top row has sequence
    if first_row[2] - first_row[1] == first_row[1] - first_row[0]:
        ans += 1
    G.append(first_row)

    second_row = list(map(lambda x: int(x), input().split()))
    G.append([second_row[0],0,second_row[1]])

    third_row = list(map(lambda x: int(x), input().split()))
    if third_row[2] - third_row[1] == third_row[1] - third_row[0]:
        ans += 1
    G.append(third_row)

    # Determine the first and right column
    if first_row[0] - second_row[0] == second_row[0] - third_row[0]:
        ans += 1
    if first_row[2] - second_row[1] == second_row[1] - third_row[2]:
        ans += 1
    
    # For both diagonals and middle row and column, determine the mean of each and count most occurrences
    # create dictionary to count occurrences
    dict1 = {}
    # top left diagonal
    if (first_row[0] + third_row[2])%2 == 0:
        middle = (first_row[0] + third_row[2])/2
        dict1[middle] = 1
    # top right diagonal
    if (first_row[2] + third_row[0])%2 == 0:
        middle = (first_row[2] + third_row[0])/2
        if middle in dict1:
            dict1[middle] += 1
        else:
            dict1[middle] = 1
    # middle column 
    if (first_row[1] + third_row[1])%2 == 0:
        middle = (first_row[1] + third_row[1])/2
        if middle in dict1:
            dict1[middle] += 1
        else:
            dict1[middle] = 1
    # middle row
    if (second_row[1]+second_row[0])%2 == 0:
        middle = (second_row[1]+second_row[0])/2
        if middle in dict1:
            dict1[middle] += 1
        else:
            dict1[middle] = 1
    
    if len(dict1) > 0:
        ans += max(dict1.values())
    print("Case #{}: {} ".format(test_case+1, int(ans)))