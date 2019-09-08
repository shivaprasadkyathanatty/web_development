try:
    f=open("/home/shivaprasad/github/web_development/PYTHON/file.txt",'r')
    for line in f:
        print (line)
except:
    print ("Can't read the file")
finally:
    f=open("/home/shivaprasad/github/web_development/PYTHON/file.txt",'a')
    f.write("\nNew Line")
    f.close()
    print ("Finally executed this")
