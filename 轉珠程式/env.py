# 0:心珠 1:水 2:火 3:木 4:光 5:暗
max_Row = 5
max_Col = 6
panel = [[0, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4]]  # 盤面
systemmod = 0  # 模式
step = [1, 1, 1, 1]  # 0:上 1:下 2:左 3:右
step_i = [0, 0]  # 起始座標 X:Y


def panel_analysis(panel, max_Col, max_Row, systemmod):
    mod = {0: "最高com"}
    bead = {}
    print("版面分析: 選用{}，版面格式 行:{}，列:{}".format(mod[systemmod], max_Row, max_Col))
    bead = bead_analysis(panel)
    print("珠子狀態:", bead)


def bead_analysis(panel):
    x = [0, 0, 0, 0, 0]
    bead = {"水": 0, "火": 0, "木": 0, "光": 0, "暗": 0}
    for c in panel:
        for i in c:
            x[i - 1] += 1
    i = 0
    for t in bead:
        bead[t] = x[i]
        i += 1
    return bead


def run(panel, step):
    point = step_i
    for i in step:
        if run_rule(point, i) is not True:
            print("無效路徑")
            continue
        if i == 0:
            panel[point[0]][point[1]], panel[point[0] - 1][point[1]] = panel[point[0] - 1][point[1]], panel[point[0]][point[1]]
            point[0] -= 1
        elif i == 1:
            panel[point[0]][point[1]], panel[point[0] + 1][point[1]] = panel[point[0] + 1][point[1]], panel[point[0]][point[1]]
            point[0] += 1
        elif i == 2:
            panel[point[0] - 1][point[1]], panel[point[0]][point[1]] = panel[point[0]][point[1]], panel[point[0]][point[1] - 1]
            point[1] -= 1
        elif i == 3:
            panel[point[0] + 1][point[1]], panel[point[0]][point[1]] = panel[point[0]][point[1]], panel[point[0]][point[1] + 1]
            point[1] += 1
        for c in panel:
            print(c)
        print(point)


def eliminate(panel):
    comber = 0
    for r in range(max_Row):
        temp = []
        for c in range(max_Col):
            for t in range(c + 1, max_Col):
                if panel[r][c] == panel[r][t]:
                    temp.append(t)
                    temp.append(c)
                else:
                    break
            for t in range(c - 1, 0, -1):
                print(c)
                if panel[r][c] == panel[r][t]:
                    temp.append(t)
                    temp.append(c)
                else:
                    break
        temp = list(set(temp))
        print(temp)
        for i in temp:
            panel[r][i] = -1
    print(panel)


def run_rule(point, i):
    if i == 0 and point[1] == 0:
        return False
    elif i == 1 and point[1] == max_Row:
        return False
    elif i == 2 and point[0] == 0:
        return False
    elif i == 3 and point[0] == max_Row:
        return False
    else:
        return True


# panel_analysis(panel, max_Col, max_Row, systemmod)
eliminate(panel)