import sys

list = [1, 2, 3]
it = iter(list)
print(it)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

