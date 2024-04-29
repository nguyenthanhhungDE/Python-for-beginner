# Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c

# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a = float(input("nhap vao a: "))
b = float(input("nhap vao b: "))
c = float(input("nhap vao c: "))

d = (a+b)**c
print(100 <= d <= 200)