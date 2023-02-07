n=input()
for i in range(len(n)):
    if i%3==0:
        n=n.replace(n[i],'3',1) 
print(n.replace('3',''))