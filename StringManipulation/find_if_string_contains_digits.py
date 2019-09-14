
def digits_checker(str):
    import re
    if re.match('^[0-9]*$', str):
        print('string contains digits')
    else:
        print('string does not contain digits')
        
print(digits_checker('abc'))
        