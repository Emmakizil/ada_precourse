def print_ten(word):
    counter = ""
    for i in range(1,11):
        counter += (f'{i} {word} ')
    return counter
        
print(print_ten("snow"))
print(print_ten(""))
print(print_ten("123"))