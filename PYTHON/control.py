if 1!=1:
    if 1>2:
        print ("True!")
    elif 2<1:
        print ("False!")
    else:
        print ("Both!")
else:
    print("Out!")

seq = [1,2,3,4,5,6]
for item in seq:
    print ("Hello")

d={"key1":"value1","key2":"value2"}
for k in d:
    print (k)
    print(d[k])

for item in d.keys():
    print (item)

for item in d.values():
    print(item)

tup_list=[(1,2),(3,4),(5,6)]
for tup1,tup2 in tup_list:
    print(tup1)
    print(tup2)
for tup in tup_list:
    print(tup)

i=1
while i<5:
    print("number is: {}".format(i))
    i = i+1


list1=[1,2,3,4]
list2=[]

for item in list1:
    list2.append(item**2)

print(list2)


out = [item**2 for item in list1]
print(out)
