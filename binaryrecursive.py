def Binary_search(arr, low, high, x): 
    if high >= low:
         mid = (high + low) // 2
         if(arr[mid] == x):
            return mid
         elif arr[mid] > x:
            return Binary_search(arr, low, mid - 1, x)
         else:
            return Binary_search(arr, mid + 1, high, x)
    else:
        return -1
arr = [ 10,48,56,62,79,84,93,102,142,152,155 ]
x = 84
result = Binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print("Elements are present at index psoition", str(result))
else:
    print("The given elements are not present in array")
