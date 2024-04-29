# Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không, nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau:
# K[i/2] = L[i]*L[i+1] (với i chẵn)

l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

for i in range(len(l)):
    if l[i].isnumeric():
        l[i] = int(l[i])

if len(l) % 2 == 0:
    kq = True
    for i in range(len(l)-1):
        if ((type(l[i]) is str and type(l[i]+1) is int) or (type(l[i]) is int and type(l[i+1] is str))):
            kq = False
    if kq:
        k=[]
        for i in range(0,len(l),2):
            k.append(l[i]*l[i+1])
        print("K=",k)
    else:
        print("K=",k)
else:
    print("không thể xây dựng được list k vì số phần tử của l là số lẻ")