words = ['Hello ', 'There ', 'This ', 'Is ', 'Inserted ', 'by ', 'Python ']
file = open('/Users/a../Desktop/ProgrammingPrinciples2/Week5/Lab5/qq.txt','w')
file.writelines(words)
file.close()