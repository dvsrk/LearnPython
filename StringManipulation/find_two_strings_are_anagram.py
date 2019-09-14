
str1='iceman'
str2='cinemak'
c_str1 = {}
c_str2 = {}

for c in str1:
    if c_str1.get(c):
        c_str1[c] = c_str1[c] + 1
    else:
        c_str1[c] = 1
    if str2.find(c) == -1:
        print('two strings are not anagrams')
        exit(0)

for c in str2:
    if c_str2.get(c):
        c_str2[c] = c_str2[c] + 1
    else:
        c_str2[c] = 1
    if str1.find(c) == -1:
        print('two strings are not anagrams')
        exit(0)

if c_str1 == c_str2:
    print('strings are anagrams')
else:
    print('strings are not anagrams')
        