"""
Given a sorted array arr[] of N integers and a number K is given. The task is to check if the element K is present in the array or not.

Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of elements in the array and the number K seperated by space. Next line contains N elements.

Output:
For each testcase, if the element is present in the array print "1" (without quotes), else print "-1" (without quotes).

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= K <= 106
1 <= arr[i] <= 106

Example:
Input:
2
5 6
1 2 3 4 6
5 2
1 3 4 5 6

Output:
1
-1

Explanation:
Testcase 1: Since, 6 is present in the array at index 4 (0-based indexing), so output is 1.
Testcase 2: Since, 2 is not present in the array, so output is -1.

"""

t=int(input())
result = []
for i in range(t):
    n,k = map(int,input().split())
    #print(n,k)
    lst = list(map(int, input().split()))
    first = 0
    last = len(lst)-1
    found = False
    while first <= last and not found:
        midpoint = (first+last)//2
        if lst[midpoint] == k:
            #print(midpoint)
            result.append(1)
            found = True
        else:
            if k < lst[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    if not found:
        result.append(-1)
print(*result, sep = "\n")    
    
                
            
