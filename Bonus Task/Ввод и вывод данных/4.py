n = int(input())
n %= (24*60)
hour = n / 60
min = n % 60
print(int(hour), int(min))
