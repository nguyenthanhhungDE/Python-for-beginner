# Nhập vào một list số nguyên L, hãy sắp xếp list L theo thứ tự từ bé đến lớn

l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

# l.sort()
# print(l)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j] > l[i]:
            l[i],l[j] = l[j],l[i]

print(l)