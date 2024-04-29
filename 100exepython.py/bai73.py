#Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
def bangcuuchuong(a, b):
    if a > b:
        for i in range(1,11):
            print(a,"x", i,"=",a*i)
    else:
        for i in range(1,11):
            print(b,"x",i,"=",b*i)

bangcuuchuong(10,5)