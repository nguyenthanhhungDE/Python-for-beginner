#Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tính và trả về giá trị trung bình của a phần tử đầu tiên trong L
def trungbinha(l,a):
    tong = 0
    for i in range(0,a):
        tong += l[i]
    return tong/a

print(trungbinha([2,3,4,5,6,7],3))