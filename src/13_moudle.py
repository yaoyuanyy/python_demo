# 部分引入
from sys import path
from sys import argv
from sys import *
import sys

for i in argv:
    print(i)
print(path)
if __name__ == '__main__':
    print("i am self")

print(dir(sys))