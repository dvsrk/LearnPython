
"""
Given an array of N elements and a integer K. Your task is to return the position of first occurence of K in the given array.
Note: Position of first element is considered as 1.

Input:
First line of input contains T denoting the number of testcases. For each testcase there will be two space separated integer N and K denoting the size of array and the value of K respectively. The next line contains the N space separated integers denoting the elements of array.

Output:
For each test case, print the index of first occurrence of given number K. Print -1 if the number is not found in array.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= K <= 106
1 <= A[i] <= 106

Example:
Input :
2 
5 16
9 7 2 16 4
7 98
1 22 57 47 34 18 66

Output : 
4
-1

"""

    t = int(input())
    results = []
    i=0
    j=0
    for j in range(t):
        n,k = map(int,input().split())
        lst = list(map(int,input().split()))
        found = 0
        for i in range(n):
            if lst[i] == k:
                found =1
                results.insert(j, i+1)
                break
        if found == 0:
                results.insert(j, -1)
    print(*results, sep="\n")
                
