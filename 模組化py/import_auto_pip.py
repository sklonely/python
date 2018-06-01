def importFix():
    lestModName = ""
    while 1:
        try:
            import sys
            import os
            # 要import的東西放這裡
            import aaa
        except ModuleNotFoundError:  # 如果找不到模組就進行pip
            err = str(sys.exc_info()[1])
            if (lestModName != err[17:-1]):
                print("缺少mod: " + err[17:-1] + " 正在進行安裝")
                os.system('pip install ' + err[17:-1])
                lestModName = err[17:-1]
            else:
                print("無法修復import問題 請人工檢查")
                print("Error mod name: " + err[17:-1])
                break
        else:
            break


importFix()