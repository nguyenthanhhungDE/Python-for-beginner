#Viết hàm có tham số đầu vào là một dictionary, hãy tạo một dictionary mới hoán đổi giá trị và key của dictionary đầu vào, rồi trả về dicionary mới đó. Nếu sau khi hoán đổi có 2 key trùng nhau (do dictionary đầu vào có 2 giá trị trùng nhau), hàm trả về None
def hoandoi_D(D):
    d_kq = {}
    for i in D:
        if D[i] not in d_kq:
            d_kq[D[i]] == i
        else:
            return None
    return d_kq

D = {"Tieng anh":"hello","Tieng viet":"xin chao","tieng phap":"Bonjour"}

print(hoandoi_D(D))