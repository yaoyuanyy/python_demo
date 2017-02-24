import codecs
import pickle
import sys

# sys.stdout("ddd")
s = "yy\n"
print(str(s))
# repr可以转义特殊字符
print(repr(s))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4), end=" \n")

table = {'google': 1, 'firefox': 2}
for k, v in table.items():
    print('{0:2}{1:3d}'.format(k, v))

print('{0[google]:2}{0[firefox]:3d}'.format(table))
# **table用法
print("{google:2}{firefox:3d}".format(**table))

# 文件什么格式，encoding就是什么值
f = open("D:\gome_doc\gome.txt", "r+", encoding='utf-8')
str1 = f.read()
print(str1)
if not f.closed:
    print("closing")
    f.close()

f2 = open("D:\gome_doc\gome.txt", "r+", encoding='utf-8')
lines = f2.readlines()
for line in range(len(lines)):
    if line != '\n':
        print("line{0:2}:{1:3}".format(line, lines[line]))
f2.close()

with open("D:\gome_doc\gome.txt", "w", encoding='utf-8') as f22:
    for line in f22:
        if '\n' in line:
            break
        print("with:", line)

# 对象存储到文件中需要先转成字符串
file3_url = "D://gome_doc//test3.txt"
f3 = open(file3_url, 'w')
value = ('com.yy', 12)
valueStr = str(value)
f3.write(valueStr)
length = f3.tell()
print("f3文件的长度是：", length)
if not f3.closed:
    f3.close()

with open(file3_url, 'r') as f4:
    v4 = f4.read()
    print('v4:', v4)
    # with会帮你关闭文件
    print(f.closed)

file_output = open("D://gome_doc//test.txt", "wb")
data = {'a': [1, 2.0, 3],
         'b': ('string', 'Unicode string'),
         'c': None}
# 序列化对象到文件中
pickle.dump(data, file_output)
file_output.close()

# 从 file 中读取一个字符串，并将它重构为原来的python对象。
input = open("D://gome_doc//test.txt", "rb")
s = pickle.load(input)
print(s)
