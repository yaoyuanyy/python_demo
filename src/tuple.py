tu = ()
tu2 = ('first',)
tu3 = (11, 'dsf', 'sfsd')*2
tu4 = (22, 'dssdfsf', 'sdfdfsfsd')
print(tu2[0])
# tu3[0] = 11 #报错
print(tu3)
tu5 = tu3 + tu4
print('tu5:', tu5)
tu6 = (22, 345, 11)

del tu2
# print(tu2)# 报错
print(tu3.count(2))

print(max(tu6))
