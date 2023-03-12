import os
print('Exist:', os.access('/Users/a../Desktop/ProgrammingPrinciples2/Week6/Lab6/builtin-functions/1.py', os.F_OK))
print('Readable:', os.access('/Users/a../Desktop/ProgrammingPrinciples2/Week6/Lab6/builtin-functions/1.py', os.R_OK))
print('Writable:', os.access('/Users/a../Desktop/ProgrammingPrinciples2/Week6/Lab6/builtin-functions/1.py', os.W_OK))
print('Executable:', os.access('/Users/a../Desktop/ProgrammingPrinciples2/Week6/Lab6/builtin-functions/1.py', os.X_OK))