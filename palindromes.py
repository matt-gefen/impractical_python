# Pseudocode
# Loop through digital dictionary as a list
# Create an empty list to hold palindromes
# Loop through each word in word list:
#   If palindrome - add to palindrome list
#   else move on
# Print Palindrome List

import load_dictionary

word_list = load_dictionary.load('dictionary.txt')
pallindromes = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pallindromes.append(word)

print('\nThere were {} palindromes in this dictionary!\n'.format(len(pallindromes)))
print(*pallindromes, sep='\n')
