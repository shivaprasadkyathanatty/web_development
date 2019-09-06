'''
def arrayCheck(nums):
    for i in nums:


arrayCheck([1,1,2,3,1])
arrayCheck([1,1,2,4,1])
arrayCheck([1,1,2,1,2,3])
'''


def end_other(str,substr):
    substr_len=len(substr)
    str_len=len(str)
    if str_len>substr_len:
        if str[str_len-substr_len:].lower()==substr.lower():
            print (True)
        else:
            print (False)
    else:
        if substr[substr_len-str_len:].lower()==str.lower():
            print (True)
        else:
            print (False)
end_other('Hiabc','abc')
end_other('AbC','HiaBc')
end_other('abc','abXabc')


def doubleChar(str):
    new_str=''
    for i in str:
        new_str=new_str+i+i
    print (new_str)

doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')


def no_teen_sum(a,b,c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def fix_teen(n):
    if n>12 & n<20:
        if n==16:
            return n
        if n==17:
            return n
        else:
            return 0
    else:
        return n

print(no_teen_sum(1,2,3))
print(no_teen_sum(2,13,1))
print (no_teen_sum(2,1,14))
print (no_teen_sum(1,16,17))
print (no_teen_sum(1,17,2))
