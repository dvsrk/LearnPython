"""

Method 1 : Using list.sort() and == operator
sort() coupled with == operator can achieve this task. We first sort the list, so that if both the lists are identical,
then they have elements at the same position. But this doesn’t take into account the ordering of elements in list.

"""

lst1 = [1, 2, 4, 3, 5] 
lst2 = [1, 2, 4, 3, 5]

if len(lst1) != len(lst2):
    print("Lists are not identical.")
else:
    lst1.sort()
    lst2.sort()
    if(lst1 == lst2):
        print("Lists are identical.")
    else:
        print("Lists are not identical.")


"""
Method 2 : Using collections.Counter()
Using Counter(), we usually are able to get frequency of each element in list, checking for it, for both the list,
we can check if two lists are identical or not.
But this method also ignores the ordering of the elements in the list and only takes into account the frequency of elements.

"""


"""
# Python 3 code to demonstrate 
# check if list are identical 
# using sum() + zip() + len() 

# initializing lists 
test_list1 = [1, 2, 4, 3, 5] 
test_list2 = [1, 2, 4, 3, 6] 

# printing lists 
print ("The first list is : " + str(test_list1)) 
print ("The second list is : " + str(test_list2)) 

# using sum() + zip() + len() to check if 
# lists are equal

for i, j in zip(test_list1, test_list2):
    if i==j:
        print(sum([1 if i ==j]))
        



if len(test_list1)== len(test_list2) and len(test_list1) == sum([1 for i, j in zip(test_list1, test_list2) if i == j]): 
	print ("The lists are identical") 
else : 
	print ("The lists are not identical") 


"""
