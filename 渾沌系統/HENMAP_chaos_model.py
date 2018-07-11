# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import math
    except (ModuleNotFoundError, ImportError):  # python import error
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    else:
        del lestModName
        break
# import自動修復 程式碼片段


class Chaos():

    def __init__(self, A, c):

        # 初始化變數type設定 全部都是 list
        self.A = []
        self.c = []
        self.ax = [1, 1, 1]
        self.dx = [0, 0, 0]
        self.g = []
        self.h = []
        self.j = []
        self.count = 0
        # 初始化 值
        self.A = A
        self.c = c

    def setModulation(self, ax, dx):

        # 設定 調變參數
        self.ax = ax
        self.dx = dx
        # 重新計算 G H J 值
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
        self.h.append(ax[2] / ax[1])
        self.h.append(-(ax[2] * dx[1]) / ax[1] + dx[2])

    def runChaos(self, k, x):
        # 參數站存
        t = []
        g = self.g
        h = self.h
        j = self.j

        if k <= 1:
            x[0] = self.ax[0] * x[0] + self.dx[0]
            x[1] = self.ax[1] * x[1] + self.dx[1]
            x[2] = self.ax[2] * x[2] + self.dx[2]

        t.append(g[0] * (x[1] * x[1]) + g[1] * x[1] + g[2] * x[2] + g[3])
        t.append(h[0] * x[0] + h[1])
        t.append(j[0] * x[1] + j[1])

        return t

    def runMaster(self, k, x):
        return self.runChaos(k, x)

    def runSlave(self, k, x, Um):
        t = self.runChaos(k, x)
        if (k > 1):
            t[0] = t[0] + self.createUs(x) + Um
        return t

    def createUk(self, X, Y):

        self.Um = self.createUm(X)
        self.Us = self.createUs(Y)
        return self.Um + self.Us

    def createUm(self, x):
        A = self.A
        c = self.c
        g = self.g
        h = self.h
        j = self.j

        Um = math.pow(x[1], 2) * g[0] + x[1] * g[1] + x[2] * g[2] + x[0] * c[0] * h[0] + x[1] * c[1] * j[0] - x[0] * A - x[1] * c[0] * A - x[2] * c[1] * A
        return Um

    def createUs(self, y):
        A = self.A
        c = self.c
        g = self.g
        h = self.h
        j = self.j

        Us = (-math.pow(y[1], 2) * g[0] - y[1] * g[1] - y[2] * g[2] - y[0] * c[0] * h[0] - y[1] * c[1] * j[0] + y[0] * A + y[1] * c[0] * A + y[2] * c[1] * A)
        return Us

    def checkSync(self, Us, Um):
        Um = round(Um, 4)
        Us = round(Us, 4)

        if (Us + Um) == 0:
            self.count += 1
            if self.count >= 10:
                return True
        else:
            return False

    def show(self):
        print('A= ', self.A, '\nc= ', self.c, '\ng= ', self.g, '\nh= ', self.h, '\nj=', self.j)
        pass
