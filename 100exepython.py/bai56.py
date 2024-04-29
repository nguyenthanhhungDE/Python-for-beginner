#Nhập vào một list số nguyên L, tìm và in ra giá trị dương đầu tiên của list, nếu không có giá trị dương, ta in ra -1

l = input("nhap vao L:")
l = l.split(",")
l = list(map(int,l))

gt_duong = -1

for i in l:
    if i > 0:
        gt_duong = i
        break
print(gt_duong)