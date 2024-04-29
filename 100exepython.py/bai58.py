# Nhập vào một list số nguyên L, nhập vào số nguyên x, tìm giá trị trong list xa x nhất

l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

x = (input("nhap vao x:"))

kq = None

for i in l:
    if kq == None or abs(kq-x) < abs(i-x):
        kq = i 

print(i)