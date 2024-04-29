# Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
a = float(input("nhap vao a:"))
b = float(input("nhap vao b:"))
c = float(input("nhap vao c:"))

if(a +b > c and a +c > b and b +c > a):
    print("a,b,c co the tao thanh 1 tam giac")
else:
    print("a, b, c khong the tao thanh 1 tam giac")