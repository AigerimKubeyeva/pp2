import re 

file=open("/Users/a../Desktop/ProgrammingPrinciples2/Week5/Lab5/qq.txt", "r")
result=re.findall("[a-z]+(_[a-z]+)+", file.read())
print(result)