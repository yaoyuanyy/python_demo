ss = ["2323", "111", "sesffaefa"]
for s in ss[:]:
    if len(s) > 5:
        ss.insert(0, s)
print(ss)


for i in range(0, 15, 3):
    print(i)

for i in range(len(ss)):
    print(i,  ss[i])

print(list(ss))

for i in range(2, 10):
    if i % 2 == 0:
        print("偶数", i)
        continue 
    print("奇数", i)

v1 = [1, 2, 3]

v2 = [(x, x*2) for x in v1 if x > 1]
print(v2)
