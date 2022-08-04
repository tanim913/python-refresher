ar, st = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
setA = set(map(int, input().split(' ')))
setB = set(map(int, input().split(' ')))

cnt = 0

for i in arr:
    if i in setA:
        cnt = cnt+1
    if i in setB:
        cnt = cnt-1
print(cnt)
