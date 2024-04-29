#Viết hàm đưa vào 1 dictionary có các phần tử có key là chuỗi, tìm và trả về giá trị của key có độ dài lớn nhất
def timkeymax(d):
    kq = None
    for i in D:
        if kq == None or d[kq] < kq[i]:
            kq = i
    return kq

D={"hello":10,"hpcksjbshdbhsd":15}
print(timkeymax(D))
