# print('{0:.25f}'.format(0.1))
# print(float(2**100).as_integer_ratio())

n = int(input())
x = float(input())
k = float(input())
i = 1

while i <= n:
    k1 = float(input())
    k = k * x + k1
    i += 1

print('{0:.6f}'.format(k))
