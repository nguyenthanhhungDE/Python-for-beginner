# Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tìm và trả về một list mới có số phần tử là a, giá trị các phần tử là các số nguyên tố tìm được trong list L
def de(l,a):
    for i in range(2,n//2+1):
        if n % i ==0 :
            return False
    return True

def asnt(l,a):
    l_kq = []
    for i in l:
        if asnt(i):
            l_kq.append(i)
            if len(l_kq) == a:
                return l_kq
    return l_kq

print(asnt([3,5,7,8,9,2],7))
