'''
    Selection Sort Time Complexity
    Best	Average	    Worst
    O(n^2)      O(n^2)      O(n^2)
    
'''

lst = list(map(int, input().split()))

for i in range(len(lst)):
    min_index = i
    for j in range(i+1, len(lst)):
        if lst[min_index] > lst[j]:
            min_index = j
    temp = lst[i]
    lst[i] = lst[min_index]
    lst[min_index] = temp

print(lst)