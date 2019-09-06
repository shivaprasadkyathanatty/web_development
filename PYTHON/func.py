def somefunc(parameter1="default"):
    """
    function prints value sent in the parameter
    """
    print("{}".format(parameter1))

somefunc()
somefunc("hello")

def add_num(num1,num2):
    """
    adds two parameter
    """
    if type(num1)==type(num2)==type(10):
        print (num1+num2)
    else:
        print("enter valid integers")

#result=add_num(1,2)
#print (result)
add_num(10,"20")



num_list=[1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2==0

res=even_bool(4)
print(res)

even_list=filter(even_bool,num_list)
print(list(even_list))


print(list(filter(lambda num:num%2==0,num_list)))

print('x' in [1,2,3,'x'])
