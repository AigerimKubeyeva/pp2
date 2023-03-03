from datetime import * 
print('PRINT FIRST DATE')
first = datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")),  int(input("Hour: ")),  int(input("Minute: ")),  int(input("Second: ")),  int(input("Microsecond: ")))
print('PRINT SECOND DATE')
second= datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")),  int(input("Hour: ")),  int(input("Minute: ")),  int(input("Second: ")),  int(input("Microsecond: ")))
y = first - second
print('The difference between two dates in seconds is:', y.total_seconds())