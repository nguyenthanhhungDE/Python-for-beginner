# Nhập vào một list số nguyên L, hãy đếm số lượng giá trị trong list thỏa tính chất: “lớn hơn tất cả các giá trị đứng đằng trước nó”
l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))
dem=0
for i in range(len(l)):
    kt = True
    for j in range(i):
        if l[j] >= l[i]:
            kt=False
            break
    if kt:
        dem +=1

print(dem)
