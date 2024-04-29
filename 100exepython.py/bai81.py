#Viết hàm đưa vào 1 list số nguyên L và 1 số nguyên dương a. Hãy tìm và trả về giá trị lớn thứ a trong list L (nếu a = 1 thì tìm giá trị lớn nhất, a = 2 thì tìm giá trị lớn nhì, a = 3 thì tìm giá trị lớn ba,...)
def giatrilonthua(l,a):
    for i in range(a):
        vt_max = None
        for j in range(len(l)):
            if vt_max == None or l[vt_max] < l[j]:
                vt_max = j
        if i == a -1:
            return l[vt_max]
        else:
            l[vt_max] = None
