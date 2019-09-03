
'''
Bubble Sort Time complexity:

      Best      Average     Worst
      O(n)      O(n^2)	    O(n^2)


'''


lst = list(map(int,input().split()))
print(lst)

for i in range(len(lst)):
    for j in range(len(lst)-1): # the range should be length of list minus 1 because the list will go out of bound when you increment +1
        if lst[j+1] < lst[j]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)
