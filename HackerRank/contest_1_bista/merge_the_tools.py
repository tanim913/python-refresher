def merge_the_tools(string, k):
    l = []
    m = 0
    for i in range(len(string)//k):
        l.append(string[m:m+k])
        m = m + k

    for v in l:
        print(''.join(list(dict.fromkeys(list(v)).keys())))
