# Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số nguyên tố hay không
def snt(a):
    for i in range(2,a//2+1):
        if a % i == 0:
            return False
    if a > 1:
        return True
    return False

print(snt(7))