# Nhập vào một list L có các phần tử là chuỗi (các chuỗi này không có ký tự đặc biệt, dấu câu, ký tự số, chỉ có ký tự chữ cái và khoảng trắng)

# Hãy tìm ra vị trí của chuỗi có nhiều từ nhất

l = input("nhap vao  danh sách")

l = l.split(",")

max = None

for i in range(len(l)):
    x = l[i].count(" ") + 1
    if max == None or max < x:
        max = x
        kq_vt = i

print(kq_vt)
