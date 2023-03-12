def file_lengthy(file):
    with open(file) as f:
        lines = len(f.readlines())
        return lines

file = r'/Users/a../Desktop/ProgrammingPrinciples2/Week5/Lab5/qq.txt'
print("Number of lines in the file: ",file_lengthy(file))