#prints out the first n rows of Pascal's triangle. Accepts the number n, the number of rows to print

from math import factorial

n = 7
for i in range(n):
    for j in range(n-i+1):
        print (end=" ")
    for j in range(i+1):
        print (factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()
    