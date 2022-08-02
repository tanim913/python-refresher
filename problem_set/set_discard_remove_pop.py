n = int(input())
inp = input().split()
st = set()
index = 0
for i in range(n):
    st.add(int(inp[index]))
    index = index + 1

operation = int(input())

for i in range(operation):
    cmd = input()
    if "pop" in cmd:
        if st is not {}:
            st.pop()
    elif "discard" in cmd:
        tmp = cmd.split()
        item = int(tmp[1])
        st.discard(item)
    elif "remove" in cmd:
        tmp = cmd.split()
        item = int(tmp[1])
        if item in st:
            st.remove(item)
print(sum(st))
