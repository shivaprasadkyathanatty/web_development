mylist=[1,2,3]
print(mylist)
print(len(mylist))
mylist[0]="New Item"
print(mylist)
mylist.append([4,5,6])
print(mylist)
mylist.extend([7,8,9])
print(mylist)
mylist.pop(0)
print(mylist)
mylist.reverse()
print(mylist)
mylist=[3,1,5,2]
mylist.sort()
print(mylist)
mylist=[1,2,['x','y','z']]
new = mylist[2][0]
print(new)
mylist = [[1,2,3],[4,5,6],[7,8,9]]
firstcol=[row[0] for row in mylist]
print (firstcol)
