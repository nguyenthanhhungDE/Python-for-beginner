# Nhập vào một list số nguyên L, Hãy tìm và in ra một vị trí trong L thỏa hai điều kiện: có hai giá trị lân cận và giá trị tại vị trí đó bằng tích hai giá trị lân cận. Nếu L không tồn tại giá trị như vậy thì in ra - 1


l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

kq= -1

for i in range(1, len(l) -1):
    if l[i] == l[i-1]*l[i+1]:
        kq = i 
        break
print("vi tri thoa yeu cai de là:",i)