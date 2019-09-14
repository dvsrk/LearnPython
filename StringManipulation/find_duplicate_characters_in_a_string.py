

str = 'xxxyyyzzz'
counter={}

for c in str:
    if counter.get(c):
        counter[c] = counter[c]+1
    else:
        counter[c] = 1

print(counter)

for k in counter:
    if counter[k] > 1:
        print(k, counter[k])
