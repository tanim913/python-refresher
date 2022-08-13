inp = str(input())
cnt = 1
ls = []
ls2 = [" "]
move_back = False
curr_num = 0
if inp.strip() == "git init":
    while True:
        com_msg = input(str()).split(" ")

        if com_msg[0] == "git":

            if com_msg[1] == "commit":
                curr_num = cnt
                move_back = False
                com_msg_str = ' '.join(str(x) for x in com_msg[2:])
                x = str(cnt) + " " + com_msg_str
                ls.append(x)
                cnt += 1

            if com_msg[1] == "show" and com_msg[2] == "commit":
                temp = ls[len(ls) - 1].split(" ")
                print(' '.join(str(x) for x in temp[1:]))

            if com_msg[1] == "show" and com_msg[2] == "all" and com_msg[3] == "commit":
                for i in range(len(ls) - 1, -1, -1):
                    if not move_back:
                        if i == len(ls) - 1:
                            y = '*' + str(ls[i])
                            print(y)
                        else:
                            print(ls[i])
                    if move_back:
                        if i == len(ls) - 2:
                            y = '*' + str(ls[i])
                            print(y)
                        else:
                            print(ls[i])

            if com_msg[1] == "delete":
                if len(ls) != 0:
                    key = int(com_msg[2])
                    for i in range(0, len(ls), 1):
                        if key == int(ls[i][0]):
                            del ls[i]
                            break
                else:
                    print("No commit left to delete")

            if com_msg[1] == "jump":
                t = ""
                key = int(com_msg[2])
                # print(key)
                for i in range(0, len(ls), 1):
                    if key == int(ls[i][0]):
                        t = ls[i]
                        del ls[i]
                        break
                ls2[0] = t
                ls = ls + ls2

            if com_msg[1] == "move" and com_msg[2] == "back":
                move_back = True

            if com_msg[1] == "update":
                tm = ' '.join(str(x) for x in com_msg[2:])
                digit = (ls[len(ls) - 1][0])
                ls[len(ls) - 1] = digit + " " + tm

        if com_msg[0].strip() == "exit":
            break
else:
    print("Re-run the code and enter 'git init'")
