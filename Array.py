from array import *

arr = array('i',[1,3,56,7,8,2,9,2,3])
#acess
print(arr[0])
print(arr)

#insert
arr.insert(2,55)

print(arr)

#delete
arr.pop(2)
print(arr)

#search
search_element = 56
for number in range(0,len(arr)):
    if arr[number] == search_element:
        print(f"Index :{number} Value :{arr[number]}")
        break
print(arr)