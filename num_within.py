#check whether a number falls in a given range

def ranges(n):
    if n in range(7,11):
        print( " %s is in the range"%str(n))
    else:
        print(" %s is outside of range"%str(n))
ranges(8) 
ranges(99)
ranges(1)
ranges(9)