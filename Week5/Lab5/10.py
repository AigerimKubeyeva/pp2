import re

file=open("/Users/a../Desktop/ProgrammingPrinciples2/Week5/Lab5/qq.txt", "r")
result=re.sub(r"(\w)([A-Z])", r"\1 \2", file.read())
print(result)