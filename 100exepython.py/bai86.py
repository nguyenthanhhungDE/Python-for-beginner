# Một nhà hàng có các món ăn: Gà rán, hamburger, cocacola

# Giá của gà rán là: 30.000đ
# Giá của hamburger là: 25.000đ
# Giá của cocacola là: 10.000đ
# Yêu cầu người dùng nhập vào số lượng từng món ăn.

# Sau đó in ra hóa đơn theo dạng như sau:

print("Chao mung cai ban den voi nha hang thuc an nhanh!")
print("moi ban nhap so luong tung moi an")
print()
sl_garan = int(input("ga ran: "))
sl_ham = int(input("hamberger: "))
sl_coca = int(input("cocacola :"))

print()

def dinhdang(s):
    while (len(s)) < 20:
        s +=" "
    return s

print(" hoa don: ")
print(dinhdang("ga ran")+ "30.000 x" + str(sl_garan))
print(dinhdang("hambergo")+ "25.000 x" + str(sl_ham))
print(dinhdang("cocacola")+ "10.000 x" + str(sl_coca))
print("Tong: ")

def phancachngan(a):
    a = str(a)  
    i = len(a) - 3
    while i > 0:
        a = a[:i] + "." a[i:]
        i  -=3
    return a

