# Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L
L = input("nhap vao list so nguyen:")
L = L.split(",")
L = list(map(int, L))

max = None
for i in L:
    if max ==None or max < i :
        max = i
print(max)