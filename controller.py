# 從 Brython 引入 document 並以 doc 為別名
from browser import document as doc
# 從 Brython 引入 localStorage
from browser.local_storage import storage
# 引入 Encrypt 類別
from encrypt import Encrypt
# 設定預計用作編碼物件的全域變數
e = None
# 設定使用者輸入的全域變數
userinput = ""
# 設定暫存結果的全域變數
result = ""
# 設定輸入欄位為視窗焦點
doc["input"].focus()

# 按下新建按鈕的事件
def new_function(event):
    # 宣告編碼物件的全域變數
    global e
    # 建立新的編碼物件
    e = Encrypt()
    # 在狀態列顯示密碼表
    doc["result"].innerHTML = str(e)
    # 設定輸入欄位為視窗焦點
    doc["input"].focus()

# 按下儲存按鈕的事件
def save_function(event):
    # 宣告編碼物件的全域變數
    global e
    # 先測試是否有按過新建按鈕
    if e == None:
        # 在底下狀態列顯示無法儲存的提示訊息
        doc["result"].innerHTML = "出錯了唷！無法儲存"
    else:
        # 有按過新建按鈕就進行存檔工作
        storage["code"] = str(e)[6:]
        # 在底下狀態列顯示工作完成的訊息
        doc["result"].innerHTML = storage["code"] + " 已儲存"
    # 設定輸入欄位為視窗焦點
    doc["input"].focus()

# 按下載入按鈕的事件
def load_function(event):
    # 宣告編碼物件的全域變數
    global e
    # storage 可能會發生例外
    try:
        # 利用 storage 建立新編碼物件
        e = Encrypt(storage["code"])
        # 底下狀態列顯示載入完成的訊息
        doc["result"].innerHTML = storage["code"] + "  已載入"
    except KeyError:
        # 沒有存檔會發生 KeyError
        doc["result"].innerHTML = "出錯了唷！尚未存檔"
    # 設定輸入欄位為視窗焦點
    doc["input"].focus()

# 按下編碼按鈕的事件
def encode_function(event):
    # 宣告全部的全域變數
    global e, userinput, result
    # 取得使用者輸入
    userinput = doc["input"].value
    # 先測試使用者是否有輸入
    if userinput == "":
        # 在底下狀態列顯示沒有輸入的訊息
        doc["result"].innerHTML = "沒有輸入文字唷！"
    else:
        # 繼續判斷是否有編碼物件
        if e == None:
            # 在底下狀態列顯示沒有編碼物件的訊息
            doc["result"].innerHTML = "出錯了唷！無法編碼"
        else:
            # 使用者有輸入並且有按過新建按鈕
            result = e.toEncode(userinput)
            # 將編碼結果顯示在輸出欄位
            doc["output"].value = result
            # 在底下狀態列顯示相關訊息
            doc["result"].innerHTML = "編碼結果如上"
    # 設定輸入欄位為視窗焦點
    doc["input"].focus()

# 按下解碼按鈕的事件
def decode_function(event):
    # 宣告全部的全域變數
    global e, userinput, result
    # 取得使用者輸入
    userinput = doc["input"].value
    # 先測試使用者是否有輸入
    if userinput == "":
        # 在底下狀態列顯示沒有輸入的訊息
        doc["result"].innerHTML = "沒有輸入文字唷！"
    else:
        # 再測試是否有按過新建按鈕
        if e == None:
            # 在底下狀態列顯示沒有編碼物件的訊息
            doc["result"].innerHTML = "出錯了唷！無法解碼"
        else:
            # 使用者有輸入並且有按過新建按鈕
            result = e.toDecode(userinput)
            # 將解碼結果顯示在輸出欄位
            doc["output"].value = result
            # 在底下狀態列顯示相關訊息
            doc["result"].innerHTML = "解碼結果如上"
    # 設定輸入欄位為視窗焦點
    doc["input"].focus()

# 按下清除按鈕的事件
def clear_function(event):
    # 宣告編碼物件的全域變數
    global e
    # 將編碼物件設定為 None
    e = None
    # 將使用者輸入設定為空字串
    userinput = ""
    # 將暫存結果設定為空字串
    result = ""
    # 將輸入欄位設定為空字串
    doc["input"].value = ""
    # 將輸出欄位設定為空字串
    doc["output"].value = ""
    # 清空所有 localStorage 儲存內容
    storage.clear()
    # 在底下狀態列顯示相關訊息
    doc["result"].innerHTML = "已清除所有資料"
    # 設定輸入欄位為視窗焦點
    doc["input"].focus()

# 按下拷貝按鈕的事件
def copy_function(event):
    # 宣告編碼結果的全域變數
    global result
    # 先測試是否有編碼結果
    if result == "":
        # 在底下狀態列顯示拷貝失敗的訊息
        doc["result"].innerHTML = "無法拷貝！"
    else:
        # 選取輸出欄位的文字
        doc["output"].select()
        # 將結果拷貝到系統剪貼簿
        doc.execCommand("copy")
        # 在底下狀態列顯示拷貝成功的訊息
        doc["result"].innerHTML = "已拷貝"
    # 設定輸入欄位為視窗焦點
    doc["input"].focus()

# 替按鈕註冊連結的事件
doc["new"].bind("click", new_function)
doc["save"].bind("click", save_function)
doc["load"].bind("click", load_function)
doc["encode"].bind("click", encode_function)
doc["decode"].bind("click", decode_function)
doc["clear"].bind("click", clear_function)
doc["copy"].bind("click", copy_function)

# 檔名: controller.py
# 說明:《Python入門指南》的範例程式
# 網站: http://kaiching.org
# 作者: 張凱慶
# 時間: 2023 年 7 月
