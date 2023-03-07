import re

file=open('/Users/a../Desktop/ProgrammingPrinciples2/Week5/Lab5/qq.txt', "r")
result=re.findall("[A-Z]+[a-z]+", file.read())
print(result)