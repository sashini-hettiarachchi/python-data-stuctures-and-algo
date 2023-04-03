from array import *

arr = array('i', [1,2,3,4,5,6]) # Array Creation O(1)

print("This is the original array: ",arr)

arr.append(1) # Add element end of the array = o(1)

print("This is the array after appending one element @ end: ",arr)

arr.insert(2,7) # Insert element in array any position except end = O(n)

print("This is the array after inserting one element to the 3rd position: ",arr)

for element in arr:
    print("Element", element) # Array traversing O(n)

arr[4] # Access element from array O(1)

arr.remove(3) # Delete array any element except end element = O(n)

arr.pop() # Delete last element of the array = O(1)