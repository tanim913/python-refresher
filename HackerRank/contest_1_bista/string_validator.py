
def string_val(str):
    lst = list(str)
    alphanum = alpha = digit = lower = upper = False
    for i in lst:
        if i.isalnum():
            alphanum = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


if __name__ == '__main__':
    s = input()
    string_val(s)
