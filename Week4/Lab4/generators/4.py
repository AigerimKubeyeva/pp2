def squares(n,m):
    for i in range(n, m+1):
        yield i**2

a = int(input())
b = int(input())
for i in squares(a,b):
    print(i)