
"""

Given a sorted array arr[] of distinct elements which is rotated at some unknown point, the task is to find the maximum element in it.

Examples:

Input: arr[] = {3, 4, 5, 1, 2}
Output: 5

Input: arr[] = {1, 2, 3}
Output: 3

Approach: A simple solution is to traverse the complete array and find maximum. This solution requires O(n) time.
We can do it in O(Logn) using Binary Search. If we take a closer look at above examples, we can easily figure out the following pattern:

The maximum element is the only element whose next is smaller than it. If there is no next smaller element, then there is no rotation (last element is the maximum). We check this condition for middle element by comparing it with elements at mid – 1 and mid + 1.
If maximum element is not at middle (neither mid nor mid + 1), then maximum element lies in either left half or right half.
If middle element is greater than the last element, then the maximum element lies in the left half.
Else maximum element lies in the right half.

"""

lst = list(map(int, input().split()))

first= 0
last=len(lst)-1
mid= (first+last)//2

while first <= last:
    if mid == last:
        print(lst[mid])
        break
    if lst[mid] > lst[mid+1]:
        print(lst[mid])
        break
    elif lst[mid] < lst[mid+1]:
        first=mid+1
        mid = (first+last)//2
        
        
    







