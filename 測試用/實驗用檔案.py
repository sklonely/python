a = 'thread-11728982-1-BX4TQDHP.html'
a = a.split("-1-")

for i in range(10):
    b = a[0] + "-" + str(i + 1) + "-" + a[1]
    print(b)
