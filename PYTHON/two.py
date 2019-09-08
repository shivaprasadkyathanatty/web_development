import one
def func():
    print ("it's inside two.py func()")
one.func()
print ("TOP OF TWO.PY")
if __name__ == '__main__':
    print ("it's inside two.py main")
else:
    print ("two.py is imported")
