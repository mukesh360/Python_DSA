from ctypes.wintypes import tagMSG

num_list = [1,2,4,5,33,44,55,66,99] #binary search only works in Sorted array

target = int(input('Target : '))

left = 0
right = len(num_list) - 1

while left <= right :
    middle = (left + right) // 2
    if num_list[middle] == target:
        print(f"Element Found at Index : {middle}  and Element is :{target}")
        break
    elif  target < num_list[middle]:
        right = middle - 1
    elif  target > num_list[middle]:
        left = middle + 1
else :
    print('Element not Found ',target)
