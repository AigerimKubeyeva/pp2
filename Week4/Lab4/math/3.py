'''
Write a Python program to calculate the area of regular polygon.

Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625

'''
from math import * 
n=int(input()) 
lenght=int(input())
perimetr=n*lenght
apothem=lenght/(2*(tan(pi/n)))
area=(apothem*perimetr)/2

print(round(area))