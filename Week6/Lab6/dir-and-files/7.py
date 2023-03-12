with open(r"/Users/a../Desktop/ProgrammingPrinciples2/Week6/Lab6/dir-and-files/A.txt") as f:
    with open(r"/Users/a../Desktop/ProgrammingPrinciples2/Week6/Lab6/dir-and-files/A.txt", "w") as f1:
        for line in f:
            f1.write(line)