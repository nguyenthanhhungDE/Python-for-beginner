#Viết hàm đưa vào một list số nguyên và một số nguyên dương k. Hãy tìm và trả về vị trí của phần tử đầu tiên có giá trị k trong list số nguyên, nếu không có thì trả về -1
def timvitri(l,k):
    for i in range(len(l)):
        if l[i] == k:
            return i
    return -1

print(timvitri([3,6,5,2,1,4]))