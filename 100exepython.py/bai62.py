#Nhập vào một list số nguyên L, hãy kiểm tra xem L có phải là một cấp số cộng hay không? Nếu có thì tìm và in ra công sai, nếu không có thì in ra None

l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

kq = True

for i in range(len(l) - 1):
    if l[i+1] - l[i] != l[1] - l[0]:
        kq = False
        break

if kq:
    print("L la mot cap so cong voi cong sai",l[1] - l[0])
else:
    print(None)