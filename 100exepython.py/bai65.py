# # 
# Người ta định nghĩa một list số nguyên được gọi là “dạng sóng” khi tất cả các phần tử đều lớn hơn hoặc nhỏ hơn hai phần tử xung quanh nó.

# Nhập vào một list số nguyên L và kiểm tra xem L có phải là list “dạng sóng” hay không, nếu có thì ta in ra True, không có thì ta in False

l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

kq = True
for i in range(i,len(l)-1):
    if l[i-1] < l[i] > l[i+1] or l[i-1] > l[i] < l[i+1]:
        kq = False
        break
print(kq)
