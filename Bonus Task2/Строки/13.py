s=input()
sum=0
for i in range(len(s)):
    if i%3 == 0:
        s=s.replace(s,'',1)
        sum+=1
print (s)