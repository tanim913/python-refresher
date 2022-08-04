from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
l = []

for i in range(n):
    a = input()
    d[a].append(i+1)

for i in range(m):
    b = input()
    l = l + [b]
for i in l:
    if i in d:
        print(' '.join(map(str, d[i])))
    else:
        print("-1")
