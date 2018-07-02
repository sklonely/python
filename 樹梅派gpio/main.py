import RPi.GPIO

import time

# 指定GPIO口的選定模式為GPIO引腳編號模式（而非主板編號模式）

RPi.GPIO.setmode(RPi.GPIO.BCM)

# 指定GPIO14（就是LED長針連接的GPIO針腳）的模式為輸出模式

# 如果上面GPIO口的選定模式指定為主板模式的話，這裡就應該指定8號而不是14號。

RPi.GPIO.setup(14, RPi.GPIO.OUT)

# 循環10次

for i in range(0, 10):
    # 讓GPIO14輸出高電平（LED燈亮）
    RPi.GPIO.output(14, True)
    # 持續一段時間
    time.sleep(0.5)
# 讓GPIO14輸出低電平（LED燈滅）
RPi.GPIO.output(14, False)
# 持續一段時間
time.sleep(0.5)
# 最後清理GPIO口（不做也可以，建議每次程序結束時清理一下，好習慣）
RPi.GPIO.cleanup