s = input()
a = s[:s.find('h')] 
#print(a)
b = s[s.find('h'):s.rfind('h') + 1]
#print(b)
c = s[s.rfind('h') + 1:]
#print(c)
s = a + b[::-1] + c
print(s)