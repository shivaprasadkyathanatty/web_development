def stringBits(string_old):
    new_str=""
    for i in range(len(string_old)):
        if i%2 != 0:
            new_str = new_str + string_old[i]
        return new_str
print(stringBits('Hello'))


def arrayCheck(list):
    for i in range(len(list)-2):
        if list[i]==1 and list[i+1]==2 and list[i+2]==3:
            return True
    return False

print(arrayCheck([1,1,2,4,1]))
print(arrayCheck([1,1,2,3,1]))
print (arrayCheck([1,1,2,1,2,3]))



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
    if 12<n<20:
        if n==16:
            return n
        elif n==17:
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


def count_events(list):
    new_list=[]
    for i in list:
        if i%2==0:
            new_list.append(i)
    return new_list


even_list= count_events([2,1,2,3,4])
print (len(even_list))

n=11
if n in [11,12,13,14]:
    print (n)
else:
    print ('nothing')
