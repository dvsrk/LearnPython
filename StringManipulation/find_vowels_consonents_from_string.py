
def get_count_of_vowels_and_consonents(str):
    counts={'vowels':0,'consonents':0}
    
    str = str.lower()
    for i in list(str):
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or  i == 'u'):
            counts['vowels'] = counts['vowels'] + 1
        else:
            counts['consonents'] = counts['consonents'] + 1
    
    return(counts)

print(get_count_of_vowels_and_consonents('siva'))
