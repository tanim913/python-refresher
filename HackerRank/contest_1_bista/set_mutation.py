len_set = int(input())

st = set(map(int, input().split()))

op = int(input())

for i in range(op):
    operation = input().split()
    if operation[0] == 'intersection_update':
        tmp = set(map(int, input().split()))
        st.intersection_update(tmp)
    elif operation[0] == 'update':
        tmp = set(map(int, input().split()))
        st.update(tmp)
    elif operation[0] == 'symmetric_difference_update':
        tmp = set(map(int, input().split()))
        st.symmetric_difference_update(tmp)
    elif operation[0] == 'difference_update':
        tmp = set(map(int, input().split()))
        st.difference_update(tmp)

print(sum(st))
