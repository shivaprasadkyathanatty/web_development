arr=[10,12,90,70,30]
print(arr)
val = 50
pos = 2
size=len(arr)
for i in range(size,pos,-1):
    arr[i]=arr[i-1]
    print (arr[i])
    print (arr[i-1])
#     arr[i]=arr[i-1];
# arr[pos]=val
# print (arr)
