# Viết hàm đưa vào 1 list có các phần tử là chuỗi, tìm và trả về chuỗi ngắn nhất trong list
def vitrichuoi(l):
    kq = None
    for i in l:
        if kq == None or len(kq) > len(i):
            kq = i
    return kq

print(vitrichuoi(["xin chao","hahaah hu hu"]))