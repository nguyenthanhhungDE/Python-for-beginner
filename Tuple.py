# Tuple trong Python

# 1.Tạo tuple
tuple_1 = ("a", 3)
tuple_2 = ("a", ) #tuple với 1 phần tử, ("a") là str rồi
print(tuple_1)
print(type(tuple_1))

#--------------duyệt qua các phần tử của tuple
tuple_3 = ("a", 3, 4, "b")
# print(f"Chiều dài của tuple:{len(tuple_3)}")
for item in tuple_3:
    print(item)

# 3.cộng các tuples
tuple_1 = ("a",3,4,"b")
tuple_2 = ("a32", 30, 4,"b")

new_tuple = tuple_1 + tuple_2

print(f"New tuple: {new_tuple}")

# 4
tuple_1 = ("a", 3 , 4, "b")
list_1 = list(tuple_1)
list_1.append("hello")
# list_1.remove(2)
new_tuple = tuple(list_1)

print(f"new tuple: {new_tuple}")

#
tuple_1 = ("a", 3, 4, "b")
tuple_2 = ("a", 3, 4, "b")

print(f"ID of tuple_1 {id(tuple_1)}")
print(f"ID of tuple_1 {id(tuple_2)}")


