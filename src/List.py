list = [1, 2, 3]

list2 = [(3*x, x**2) for x in list if x < 3]
print("list2:", list2)
list3 = [[3*x, x**2] for x in list]
print("list2:", list3)

for num in list:
    print(num)

for i in range(len(list)):
    print(i, list[i])

print(list)
list[:] = []
print(type(list))

a, b = 0, 1
while b < 10:
    print(b, end="|")
    a, b = b, a + b

