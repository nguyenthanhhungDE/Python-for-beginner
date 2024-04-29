# #Nhập vào một list số nguyên L, nhập vào 2 số nguyên dương a và b (a < b < len(L))

# Tìm và in ra số nhỏ nhất trong list từ vị trí a đến vị trí b
L = input("nhap vao L:")
L = L.split(",")
L = list(map(int,L))
a = int(input("nhap vao a:"))
b = int(input("nhap vao b:"))

min = None
for i in range(a,b+1):
    if min == None or min > L[i]:
        min = L[i]

print(min)