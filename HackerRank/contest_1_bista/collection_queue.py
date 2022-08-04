from collections import Counter

n = int(input())
stk = list(map(int, input().split()))
d = Counter(stk)
price = 0
t = int(input())
for i in range(t):
    size, cost = map(int, input().split())
    if d[size]:
        d[size] = d[size] - 1
        price = price + cost
print(price)
