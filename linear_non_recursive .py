my_list = [20,35,66,79,92,15,67,33,100]
print('List has the items: ', my_list)
searchItem = int(input('Enter a number to search : '))

for i in range(len(my_list)):
    if my_list[i] == searchItem:
        found = True
        print(searchItem, ' was found in the list at index position  ', i)
        break
if found == False:
    print(searchItem, ' was not found in the list!')
