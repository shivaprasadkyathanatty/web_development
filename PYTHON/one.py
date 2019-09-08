def func():
    print ("its inside one.py func()")

print ("TOP OF ONE.PY")
if __name__ == '__main__':
    print ("its inside one.py main")
    func()
else:
    print ("imported one.py")
