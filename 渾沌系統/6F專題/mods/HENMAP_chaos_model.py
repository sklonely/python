import math


class Chaos():

    def __init__(self, A=0.00001, c=[-0.0001, 0.0001]):

        # 初始化變數type設定 全部都是 list
        self.ax = [1, 1, 1]
        self.dx = [0, 0, 0]
        self.g = []
        self.h = []
        self.j = []
        self.count = 0
        # 初始化 值
        self.A = A
        self.c = c
        self.runModulation()

    def setModulation(self, ax, dx):

        # 設定 調變參數
        self.ax = ax
        self.dx = dx
        # 重新計算 G H J 值
        del self.g, self.h, self.j
        self.g = []
        self.h = []
        self.j = []
        # print("hi")
        self.runModulation()

    def runModulation(self):

        # 參數站存
        ax = self.ax
        dx = self.dx

        # G值計算
        self.g.append(-(ax[0] / (ax[1] * ax[1])))
        self.g.append(2 * ax[0] * dx[1] / (ax[1] * ax[1]))
        self.g.append(-0.1 * ax[0] / ax[2])
        self.g.append(ax[0] * (1.76 - (dx[1] * dx[1]) / (ax[1] * ax[1]) + 0.1 * ax[0] * dx[2] / ax[2]) + dx[0])

        # H值計算
        self.h.append(ax[1] / ax[0])
        self.h.append(-(ax[1] * dx[0]) / ax[0] + dx[1])

        # j 值計算
        self.j.append(ax[2] / ax[1])
        self.j.append(-(ax[2] * dx[1]) / ax[1] + dx[2])

        # debug
        # print(self.g, self.h, self.j)

    def runChaos(self, k, x):
        # 參數站存
        t = []
        g = self.g
        h = self.h
        j = self.j
        # 第一次先做 調變
        if k <= 1:
            x[0] = self.ax[0] * x[0] + self.dx[0]
            x[1] = self.ax[1] * x[1] + self.dx[1]
            x[2] = self.ax[2] * x[2] + self.dx[2]
        # 混沌原式計算
        t.append(round(g[0] * (x[1] * x[1]) + g[1] * x[1] + g[2] * x[2] + g[3], 6))
        t.append(round(h[0] * x[0] + h[1], 6))
        t.append(round(j[0] * x[1] + j[1], 6))

        return t

    # 跑主系統渾沌狀態
    def runMaster(self, k, x):
        return self.runChaos(k, x)

    # 跑從系統渾沌狀態
    def runSlave(self, k, y, Um):
        t = self.runChaos(k, y)
        if (k > 1):
            t[0] = round(t[0] + self.createUs(y) + Um, 6)
        return t

    # UK值
    def createUk(self, X, Y):

        self.Um = self.createUm(X)
        self.Us = self.createUs(Y)
        return self.Um + self.Us

    # UM值
    def createUm(self, x):
        A = self.A
        c = self.c
        g = self.g
        h = self.h
        j = self.j

        Um = math.pow(x[1], 2) * g[0] + x[1] * g[1] + x[2] * g[2] + x[0] * c[0] * h[0] + x[1] * c[1] * j[0] - x[0] * A - x[1] * c[0] * A - x[2] * c[1] * A
        return Um

    # US值
    def createUs(self, y):
        A = self.A
        c = self.c
        g = self.g
        h = self.h
        j = self.j

        Us = (-math.pow(y[1], 2) * g[0] - y[1] * g[1] - y[2] * g[2] - y[0] * c[0] * h[0] - y[1] * c[1] * j[0] + y[0] * A + y[1] * c[0] * A + y[2] * c[1] * A)
        return Us

    # 觀看有沒有同步
    def checkSync(self, Us, Um):
        Um = round(Um, 4)
        Us = round(Us, 4)

        if (Us + Um) == 0:
            self.count += 1
            if self.count >= 10:
                return True
        else:
            return False

    # debug用
    def show(self):
        print('A= ', self.A, '\nc= ', self.c, '\ng= ', self.g, '\nh= ', self.h, '\nj=', self.j)
        pass
