def fix_teen(n):
    if n>12 & n<20:
        if n==16:
            return n
        elif n==17:
            return n
        else:
            return 0
    else:
        return n

print (fix_teen(6))
