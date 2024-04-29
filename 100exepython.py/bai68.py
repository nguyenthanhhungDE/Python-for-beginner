#Nhập vào một list số nguyên L, hãy biến đổi L bằng cách thay đổi vị trí giữa giá trị nhỏ nhất và lớn nhất
l = input("nhap vao  danh sách")

l = l.split(",")
l = list(map(int,l))

vt_max = vt_min = None
for i in range(len(l)):
    if vt_max == None or l[vt_max] < l[i]:
        vt_max = i
    if vt_min == None or l[vt_min] > l[i]:
        vt_min = i

l[vt_max], l[vt_min] = l[vt_min], l[vt_max]
print(l)

#cách 2:
def swap_min_max(L):
    if len(L) < 2:
        return L

    min_value = L[0]  # Giả sử giá trị nhỏ nhất là phần tử đầu tiên
    max_value = L[0]  # Giả sử giá trị lớn nhất là phần tử đầu tiên
    min_index = 0     # Vị trí của giá trị nhỏ nhất
    max_index = 0     # Vị trí của giá trị lớn nhất

    # Tìm giá trị nhỏ nhất và lớn nhất cũng như vị trí tương ứng
    for i in range(len(L)):
        if L[i] < min_value:
            min_value = L[i]
            min_index = i
        if L[i] > max_value:
            max_value = L[i]
            max_index = i

    # Hoán đổi vị trí của giá trị nhỏ nhất và lớn nhất
    L[min_index], L[max_index] = L[max_index], L[min_index]

    return L