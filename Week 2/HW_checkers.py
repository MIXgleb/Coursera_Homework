x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x1 + y1) % 2 == (x2 + y2) % 2) and \
        (y2 > y1) and \
        (2 * (y2 - y1) >= abs(x2 - x1) + 1):
    print('YES')
else:
    print('NO')
