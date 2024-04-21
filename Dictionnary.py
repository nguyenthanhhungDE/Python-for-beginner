# define
#khoi tao dictionary
name_age = {"Min": 5,"Na": 6, "Bong": 10}
#tao dict rong
# name_age = dict()
# name_age = {}
#truy cap
print(name_age["Na"])
#Them vao dict, update gia tri

name_age["Bong"] = 12
name_age["Nam"] =30
print(name_age)

#Duyet qua cac phan tu
# duyet qua cac key hoac duyet qua câc value hoặc cả 2 cùng lúc
for k in name_age.keys():
    print(k)

for k in name_age.values():
    print(k)

for k, v in name_age.items():
    print(k,v)


