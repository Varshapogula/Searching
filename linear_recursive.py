def Linear_search(my_list, x):
     for i in range(len(my_list)):
         if my_list [i] == x:
             return i
     return -1


my_list= [62,58,29,75,11]
x=int(input("Enter a number that you want to search in the given list : "))

Linear_search(my_list, x)
print("Index position of the search element in the list is : ",Linear_search(my_list, x))