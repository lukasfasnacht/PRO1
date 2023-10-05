random = ['a', ('b', 'cd'), [3, 4]]

print(random[2])
print(random[0])
print(random[2][1])
print(random[1][0])
print(random[1][1][1])
print(random[1][1])

list = ['larry', 'curly', 'moe']
list_extension = ["yyy", "zzz"]

list.append("shemp")
list.insert(0, "xxx")
list.append(list_extension)
list.remove("curly")

print(list)