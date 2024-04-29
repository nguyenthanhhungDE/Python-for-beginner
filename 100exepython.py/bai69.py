# Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy tìm và in ra chuỗi có độ dài lớn nhất và số nguyên có giá trị nhỏ nhất
l = input("nhap vao l:")
l = l.split(",")

so_min = None
chuoi_max = None

for i in range(len(l)):
    if l[i].isnumeric():
        l[i] = int(l[i])
        if so_min == None or so_min > l[i]:
            so_min = l[i]
    else:
        if chuoi_max == None or len(chuoi_max) < len(l[i]):
            chuoi_max = l[i] 

print("Gia trị số nhỏ nhất trong chuỗi là ", so_min)
print("Gia tri chuoi co dọ dài lớn nhất là", chuoi_max)