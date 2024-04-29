# Nhập vào một list L có các phần tử là chuỗi.
# Hãy tìm ra chuỗi có vị trí ký tự in hoa lớn nhất

l = input("nhap vao  danh sách")

l = l.split(",")

chuoi_kq = None
vt_max = None
for i in l:
    kq = -1
    for j in range(len(i)):
        if i[j].isupper():
            kq = i
    if chuoi_kq == None or vt_max < kq:
        chuoi_kq = i
        vt_max = kq

print(chuoi_kq)