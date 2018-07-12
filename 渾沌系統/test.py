from HENMAP_chaos_model import Chaos

X = [-1.3156345, -1.84, 0.5624]
Y = [1.7, -1.2, 1.212345]

Um = 0
Us = 0

sendData = ''
getData = ''

impData = 'leadingtw_273_r124672736_周昱宏'

errorCount = 0
succsCount = 0
syncCount = 0

a = Chaos(0.01, [-0.3, 0.002])
b = Chaos(0.01, [-0.3, 0.002])
for i in range(1000):
    UK = a.createUk(X, Y)

    Um = a.createUm(X)
    X = a.runMaster(i, X)

    Us = b.createUs(Y)
    Y = b.runSlave(i, Y, Um)
    tol = [X[0] - Y[0], X[1] - Y[1], X[2] - Y[2]]
    if (tol[0] == 0):
        print(i)
        break
# a.show()