#Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list
def vitri_max(l):
    kq = None
    for i in range(len(l)):
        if kq == None or l[kq] < l[i]:
            kq = i
    return kq

print(vitri_max([7,5,4,1,3,10,5,8]))