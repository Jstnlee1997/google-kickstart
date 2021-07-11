import numpy as np

T = int(input())
for test_case in range(T):
    info1_split = list(map(lambda x: int(x), input().split()))
    N = info1_split[0]
    # M = info1_split[1]
    problems = []
    for problem_set in range(N):
        problem_interval = list(map(lambda x: int(x), input().split()))
        for problem in range(problem_interval[0], problem_interval[1]+1):
            problems.append(problem)
    S = list(map(lambda x: int(x), input().split()))

    # Make sure values in problems are unique
    problems = list(set(problems))
    ans = []
    for student in S:
        index = min(range(len(problems)), key=lambda i: abs(problems[i]-student))
        ans.append(problems[index])
        del problems[index]
    
    print("Case #{}: {} ".format(test_case+1, ' '.join(str(x) for x in ans)))
        
