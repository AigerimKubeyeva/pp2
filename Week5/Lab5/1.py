import re 

file=open('/Users/a../Desktop/ProgrammingPrinciples2/Week5/Lab5/qq.txt', "r")
res=re.findall(".*a.*b*", file.read())
print(res)