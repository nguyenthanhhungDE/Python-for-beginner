# Nhập vào một list số nguyên L, hãy đưa các số chẵn trong list về đầu list, số lẻ về cuối list và các phần tử 0 nằm ở giữa
l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))\

l_chan = []
l_le = []
l_khong = []

for i in l:
    if i ==0:
        l_khong.append(i)
    elif i % 2 == 0:
        l_chan.append(i)
    else:
        l_le.append(i)

l_kq = l_chan + l_khong + l_le
print(l_kq)