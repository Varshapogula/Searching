def Binary_search(my_list1, elem):
   low = 0
   high = len(my_list1) - 1
   mid = 0
   while low <= high:
      mid = (high + low) // 2
      if my_list1[mid] < elem:
         low = mid + 1
      elif my_list1[mid] > elem:
         high = mid - 1
      else:
         return mid
   return -1

my_list1 = [ 1, 9, 11, 21, 34, 54, 67, 90 ]
elem_to_search = 54
print("The given list of elements is : ")
print(my_list1)

my_result = Binary_search(my_list1, elem_to_search)

if my_result != -1:
   print("The search element is found at index position : ", str(my_result))
else:
   print("The search element is not found in the given list!")