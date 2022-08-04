n = int(input())
st = set(map(int, input().split()))


m = int(input())
st2 = set(map(int, input().split()))


setAns = st.difference(st2)
print(len(setAns))
