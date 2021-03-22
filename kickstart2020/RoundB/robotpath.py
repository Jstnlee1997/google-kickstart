from collections import deque

def NSEW(step, multiply, hori, vert):
    if step == 'N':
        vert -= 1*multiply
    elif step == 'S':
        vert += 1*multiply
    elif step == 'E':
        hori += 1*multiply
    else:
        hori -= 1*multiply
    return hori, vert

def final(hori, vert):
    hori += 1
    vert += 1
    if hori < 1:
        hori = hori%10**9
        if hori == 0:
            hori = 10**9
    if vert < 1:
        vert = vert%10**9
        if vert ==0:
            vert = 10**9
    print("Case #{}: {} {}".format(test_case+1, hori, vert))
    

T = int(input())
for test_case in range(T):
    steps = list(input())
    vert = 0
    hori = 0
    multiply = 1
    stack = deque()
    for step in range(len(steps)):
        if steps[step].isdigit():
            stack.append(int(steps[step]))
            multiply *= int(steps[step])
        elif steps[step] == ')':
            multiply //= stack.pop()
        elif steps[step] == 'N' or steps[step] == 'S' or steps[step] == 'E' or steps[step] == 'W':
            (hori, vert) = NSEW(steps[step], multiply, hori, vert)
    final(hori, vert)
            