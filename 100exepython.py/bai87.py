# Viết hàm cho giá trị đầu vào là list số nguyên dương L và số nguyên dương k. Hãy tạo và trả về một list L_kq có các phần tử là giá trị của phần tử xuất hiện nhiều hơn k lần trong list L theo thứ tự tăng dần
def listklan(l,k):
    l_kq = []
    for i in l:
        if l.count(i) > k:
            if i not in l_kq:
                l_kq.append(i)
    l_kq.sort()
    return l_kq
print(listklan([2,5,6,3,5,4,5,2,9,0,3,5],2))
