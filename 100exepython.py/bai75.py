#Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số Armstrong hay không

def armstrong(a):
    sochuso = len(str(a))
    while a!= 0:
        b = a % 10
        a = a // 10
        tong += b**sochuso
    if tong == a:
        return True
    return False

print(armstrong(369))
