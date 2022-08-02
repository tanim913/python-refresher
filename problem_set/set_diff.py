setA = []
setB = []

n = int(input())
for i in range(n):
    setA.append(input())

m = int(input())
for i in range(m):
    setB.append(input())

setA = set(setA)
setB = set(setB)

setAns = setA.difference(setB)
print(len(setAns))
