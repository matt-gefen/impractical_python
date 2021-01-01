# Palingram - 
# It can either have odd or even letters
# One contiguous part of the word spells a real word when read backward
# This contiguous part can occupy part or all of the core word
# The other contiguous part contains a palindromic sequence of letters
# The palindromic sequence can occupy part or all of the core word
# It does not have to be a real word unless it occupies the whole word
# The two parts cannot overlap or share letters
# The sequence is reversible

# Pseudocode - 
# Load digital dictionary as a list of words
# Start an empty list to hold palingrams
# For word in word list:
#   Get length of word:
#   if length > 1:
#       loop thorugh the letters in the word:
#           if reversed word fragment at front of word is in word list and letters after form a palindromic sequence:
#                append reverse word and word to palingram list
# sort palingram list alphabetically 
# print word-pair palingrams from palingram list


import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

def find_palingrams():
    pali_list = []
    words = set(word_list)
    for word in words:
        length = len(word)
        rev_word = word[::-1]
        if length > 1:
            for i in range(length):
                if word[i:] == rev_word[:length-i] and rev_word[length-1:] in word_list:
                    pali_list.append((word,rev_word[length-i:]))
                if word[:i] == rev_word[length-i:] and rev_word[:length-i] in words:
                    pali_list.append((rev_word[:length-i], word))
    return pali_list