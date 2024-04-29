# Nhập vào một list L, hãy tìm và in ra giá trị âm lớn nhất trong L, nếu L không có giá trị âm thì ta in 0

l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))
gt_am = 0
for i in l:
    if i < 0:
        if gt_am == 0 or gt_am < i :
            gt_am = i
print(gt_am)