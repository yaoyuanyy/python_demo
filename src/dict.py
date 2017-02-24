di = {'d1': 'd11', 'd2': 'd22'}
print(di)
print(di['d1'])
se = di.keys()
for e in se:
    print(e, di.get(e))

di2 = {11: 'd11', '1': 'd22'}
print(di2)
a = di2.items()
print('a', a)
di2[11] = 'd'
print(di2)
print('str:', str(di2))
print('len:', len(di2))
print('type:', type(di2))
del di2['1']
print(di2)
del di2
