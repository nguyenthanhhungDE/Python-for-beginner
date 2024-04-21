# 0. Tạo set và set rỗng
# my_set = {'a', 'b'}
# print(my_set,type(my_set))

my_set = set()
print(my_set, type(my_set))
# 1.Không cho phép các phần từ lặp lại
my_set = {'a', 'b', 'c', 'a'}
my_set
# 2.Check set là unorder (mỗi lần chạy lại thứ tự khác nhau)
# my_set = {'a', 'b', 'c', 'a'}

# for item in my_set
#     print(item)
#update set (hay sử dụng thêm vào set)
my_set = {'a', 'b', 'c', 'a'}
my_set.add('e')
my_set.discard('a')
print(my_set)

#Thao tác với 2 hay nhiều sets, xem thêm sơ đồ veen
my_set_1 = {'a', 'b', 'c', 'a'}
my_set_2 = {'a', 'b', 'd', 'f'}

# new_set = my_set_1.intersection(my_set_2)
# new_set = my_set_1.union(my_set_2)
new_set = my_set_1.symmetric_difference(my_set_2)
print(new_set)
