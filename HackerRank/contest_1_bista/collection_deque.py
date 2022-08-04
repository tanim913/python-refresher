from collections import deque

d = deque()
for i in range(int(input())):
    inp = input()
    if "pop" == inp:
        d.pop()
    elif "popleft" == inp:
        d.popleft()
    else:
        op, val = inp.split()
        val = int(val)
        if "append" == op:
            d.append(val)
        else:
            d.appendleft(val)
print(*d)
