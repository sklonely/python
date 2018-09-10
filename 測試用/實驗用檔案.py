import random


def c2():
    print("倒三角形")
    for i in range(0, 5, 1):
        for _ in range(i):
            print(" ", end='')
        for j in range(i, 5, 1):
            print("* ", end='')
        print()


def c1():
    print("空心菱形")
    for i in range(0, 9, 1):
        s = ""
        if i < 5:
            for _ in range(i, 4, 1):
                s += "  "
            s += "* "
            for _ in range(1, i * 2):
                s += "  "
            if i != 0:
                s += "* "
        else:
            for _ in range(10 - i, i + 1, 2):
                s += "  "
            s += "* "
            for _ in range(5 - 2 * (i - 5)):
                s += "  "
            if i != 8:
                s += "* "
        print(s)


def c3():
    while 1:
        while 1:
            # 避免出現 0XXX 數字
            num = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
            if num[0] != 0:
                break
        print(num)
        print("歡迎來到1A2B遊戲程式，請享受遊戲 ^_^\n  按下q可以退出遊戲喔~~\n")
        while 1:
            # 輸入端防呆 (防不是4位數 英文 特殊鍵)
            tip = ""
            while 1:
                try:
                    u_num = input("請猜一個4位數{}: ".format(tip))
                    if u_num == "q":
                        print("\n\n掰掰QAQ 感謝你玩他\n")
                        exit()
                    elif len(set(list(u_num))) != 4:
                        tip = "(請別重複 和 4位數.(_ _).)"
                        continue
                    u_num = int(u_num)
                    break
                except ValueError:
                    tip = "(數字阿!!!.(oAO).)"
                    pass
            # 將int 轉 list
            u_num = list(str(u_num))
            u_num = list(map(int, u_num))
            # 比較輸入與答案 A B數
            ans = [0, 0]  # a b數
            for i in range(4):
                for j in range(4):
                    if num[i] == u_num[j]:
                        if i == j:
                            ans[0] += 1
                        else:
                            ans[1] += 1
            # 勝利條件判斷
            if ans[0] == 4:
                print("恭喜你猜對了，答案是{}\n\n".format(num))
                break
            print("{}A{}B".format(ans[0], ans[1]))


# print()
# c1()
c2()
# c3()