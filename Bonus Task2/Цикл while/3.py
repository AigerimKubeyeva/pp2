num = int(input())
i = 1
while 2**i <= num:
    i += 1
print(i-1, 2**(i-1))