# 使用標準程式庫中 random 的 shuffle()
from random import shuffle

# 定義 Encrypt 類別
class Encrypt:
    # 建立 Encrypt 物件同時建立密碼表
    def __init__(self, new_code=None):
        # 設定 code
        if new_code == None:
            self.__code = [chr(i) for i in range(97, 123)]
            shuffle(self.__code)
        else:
            self.__code = list(new_code)

        # 設定 alph
        self.__alph = [chr(i) for i in range(97, 123)]

    # 回傳密碼表字串
    def __str__(self):
        code = "".join(self.__code)
        return "code: " + code

    # 編碼的方法
    def toEncode(self, original_string):
        # 暫存編碼結果的字串
        result = ""

        # 利用迴圈走完參數字串的所有字元
        for i in original_string:
            # 判斷該字元是否為英文小寫字母
            # 若是英文小寫字母就進行編碼轉換
            if i in self.__code:
                j = self.__alph.index(i)
                result += self.__code[j]
            else:
                result += i

        # 結束回傳編碼過的字串
        return result

    # 解碼的方法
    def toDecode(self, original_string):
        # 暫存解碼結果的字串
        result = ""

        # 利用迴圈走完參數字串的所有字元
        for i in original_string:
            # 判斷該字元是否為英文小寫字母
            # 若是英文小寫字母就進行解碼轉換
            if i in self.__code:
                j = self.__code.index(i)
                result += self.__alph[j]
            else:
                result += i

        # 結束回傳解碼過的字串
        return result

# 測試部分
if __name__ == '__main__':
    e = Encrypt()
    print()
    print(e)
    s1 = "There is no spoon."
    print("Input : " + s1)
    s2 = e.toEncode(s1)
    print("Encode: " + s2)
    s3 = e.toDecode(s2)
    print("Decode: " + s3)
    print()

# 檔名: encrypt.py
# 說明:《Python入門指南》的範例程式
# 網站: http://kaiching.org
# 作者: 張凱慶
# 時間: 2023 年 5 月
