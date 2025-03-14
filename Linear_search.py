from array import *

arr = array('i',[1,3,4,5,66,6,77,7,77])

search_elemnt = 10
for number in range(0,len(arr)):
    if arr[number] == search_elemnt:
        print(f"Index : {number} Value: {arr[number]}")
        break
else:
    print('Element is Not Found in the Array !!!')
