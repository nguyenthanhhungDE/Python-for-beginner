# Nhập vào một list số nguyên L, tính giá trị trung bình của list L
l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))
sum =0
for i in l:
    sum += i
print(sum/len(l))