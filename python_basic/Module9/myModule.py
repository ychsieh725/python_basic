# 計算幾次方
def pow(x, y):
    return x ** y

def get_discount(price):
    if price >= 2000:
        price -= 200*(price//2000)
    return price

# 簡單斷句






# 測試模組(固定寫法，再函式庫裡都要這樣寫，才不會在import檔案裏面出現)
if __name__ == "__main__":
    print(f"myModule.py - function pow 的結果：{pow(2, 3)}")
    print(f"myModule.py - function get-discount 的結果：{get_discount(6000)}元。")

