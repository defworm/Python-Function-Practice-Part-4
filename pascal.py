#prints out the first n rows of Pascal's triangle. Accepts the number n, the number of rows to print

from math import factorial

pascal = 7
for tier in range(pascal):
    for line in range(pascal-tier+1):
        print (end=" ")
    for line in range(tier+1):
        print (factorial(tier)//(factorial(line)*factorial(tier-line)), end=" ")
    print()
    