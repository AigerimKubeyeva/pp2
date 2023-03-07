import re

file=open("/Users/a../Desktop/ProgrammingPrinciples2/Week5/Lab5/qq.txt", "r")
result = re.sub(r'(?:_+)(\w)', lambda m: m.group(1).upper(), file.read())
print(result)


