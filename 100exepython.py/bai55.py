# Nhập vào một list số nguyên L, hãy kiểm tra xem tất cả các phần tử trong mảng có bằng nhau hay không, nếu có thì in True, không có thì in False
l = input("Nhập vào L:")
l = l.split(",")
l= list(map(int,l))

kt = True

for i in l:
    if i !=l[0]:
        kt = False
        break
if kt:
    print("List l co cac phan tu bang nhau!")
else:
    print("list L không có cac phan tu bang nhau")