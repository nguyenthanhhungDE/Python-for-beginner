#Nhập vào một list số nguyên L, hãy kiểm tra xem L có được sắp xếp từ bé đến lớn hay không, nếu có thì in True, không có thì in False
l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

kq = True
for i in rang(len(l)-1):
    if l[i] > l[i+1]:
        kq = False
        break
if kq == True:
    print("duoc sap xep tu be den lon")
else:
    print("khong duoc sap xep tu be den lon")