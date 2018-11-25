# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import base64
        from io import BytesIO
        import re
        from AESmod import AEScharp
        from PIL import Image
        from PIL import ImageDraw
        import numpy as np
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
# 若img.save()报错 cannot write mode RGBA as JPEG
# 则img = Image.open(image_path).convert('RGB')
def image_to_base64(image_path=None):
    """
    image_to_base64 顧名 把img轉成base64
    input:
        image_path type: File_path
    output:
        base64_str type: str
    """
    if type(image_path) is str:
        img = Image.open(image_path).convert('RGB')
        # print(img)
        output_buffer = BytesIO()
        img.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        base64_str = base64.b64encode(byte_data)
    else:
        output_buffer = BytesIO()
        image_path.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        base64_str = base64.b64encode(byte_data)
    return base64_str


def base64_to_image(base64_str, image_path=None):
    """
    base64_to_image 顧名 把base64轉成img
    input:
        base64_str type: str
    output:
        img type: PIL.img
    """
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    base64_data = bytes.fromhex(base64_data)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    if image_path:
        img.save(image_path)
    return img


def conv(text, lenth):
    new_text = []
    li = 0
    maxl = len(text)
    i = 0

    for i in range(lenth, maxl + 1, lenth):
        new_text.append(text[li:i])
        li = i

    if i != maxl:
        text = text[i:]
        for j in range(lenth - (maxl - i)):
            text += b" "
        new_text.append(text)
    return new_text


def chunks(lis, n):
    if n == 3:
        lis = lis[:len(lis) - len(lis) % 3]
    temp = list(lis[i:i + n] for i in range(0, len(lis), n))
    return temp


if __name__ == "__main__":
    aes = AEScharp()
    try:
        st = image_to_base64('g:/我的云端硬盘/程式/python/chaos_mod_sever/lena.png')
    except FileNotFoundError:
        st = image_to_base64('g:/我的雲端硬碟/程式/python/chaos_mod_sever/lena.png')
    print("[測試]:圖片路徑   to  base64_str", ":  ", st[:50])
    with open("base64str.txt", 'w') as f:
        f.write(str(st))
    st = base64_to_image(st.hex())
    print("[測試]:base64_str to  圖片型態", "  :  ", st)
    st = image_to_base64(st)
    print("[測試]:內存圖片   to  base64_str", ":  ", st[:50])
    st = base64_to_image(st.hex())
    print("[測試]:base64_str to  圖片型態", "  :  ", st)
