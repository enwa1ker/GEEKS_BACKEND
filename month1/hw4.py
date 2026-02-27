data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []


for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)

numbers.remove(6.13)                 
letters.append(numbers.pop(0))       
numbers.insert(1, 2)            

numbers.sort()
numbers = [i**2 for i in numbers]   

letters.reverse()

letters[1] = 'G'  
letters[-2] = 'c' 

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)

print(letters_tuple)
print(numbers_tuple)



# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

# letters = []
# numbers = []

# for item in data_tuple:
#     if isinstance(item, str):
#         letters.append(item)
#     else:
#         numbers.append(item)

# numbers.remove(6.13)

# true_val = numbers.pop(numbers.index(True))
# letters.append(true_val)

# numbers.insert(numbers.index(1), 2)

# numbers.sort()
# letters.reverse()

# letters[letters.index('C')] = 'c'
# letters[letters.index('g')] = 'G'


# numbers = [i**2 for i in numbers]

# letters = tuple(letters)
# numbers = tuple(numbers)

# print(f"letters: {letters}")
# print(f"numbers: {numbers}")