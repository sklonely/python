class ImportFix():
    def __init__(self, modname):
        self.tryFixImporTimes = 0
        while 1:
            try:
                import sys
                import os
                # 要import的東西放這裡
                import aaa
            except ModuleNotFoundError:  # 如果找不到模組就進行pip
                if(self.tryFixImporTimes < 5):
                    err = str(sys.exc_info()[1])
                    print("缺少mod: " + err[17:-1] + " 正在進行安裝")
                    os.system('pip install ' + err[17:-1])
                    self.tryFixImporTimes += 1
                else:
                    print("已嘗試" + str(self.tryFixImporTimes) + "次 import 依然有問題 請人工檢查")
                    print("Error mod name: " + err[17:-1])
                    break
            else:
                break


a = ImportFix("aaa")
