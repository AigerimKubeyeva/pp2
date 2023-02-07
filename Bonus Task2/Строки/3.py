s = input()
l = len(s)//2+len(s)%2
a = s[l:]
b = s[:l]
print(a+b)