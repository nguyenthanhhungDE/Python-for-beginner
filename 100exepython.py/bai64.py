#Người ta định nghĩa một list số nguyên là list chẵn lẻ, nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ

#Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không

l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

kq = True
for i in range(len(l) -1):
    if (l[i] + l[i+1]) % 2 ==0 :
        kq = False
        break

if kq:
    print("L là list chang le!")
else:
    print("L khong la list chan le")