print('enter the string:')
string=input()
lower=0
upper=0
for i in string:
	if(i.islower()):
			lower+=1
	if(i.isupper()):
			upper+=1
print("num of lower case characters is:", lower)
print("num of upper case characters is:", upper)

