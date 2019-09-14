

def permutation(str):
    if len(str) == 0:
        return []
    if len(str) == 1:
        return([str])
    
    l = []
    for i in range(len(str)):
        first = str[i]
        rem_lst = str[:i] + str[i+1:]
        
        for p in permutation(rem_lst):
            l.append([first] + p)
    return l
        
        

str = 'siva'
lst = list(str)
permutations = permutation(lst)
for p in permutations:
    print(''.join(p))