# To form Pig Latin, you take an English word that begins with a consonant,
# move that consonant to the end, and then add “ay” to the end of the word.
# If the word begins with a vowel, you simply add “way” to the end of the
# word. 

# Psuedocode
# Introduce program
# Take user input
# If word begins with consonant, move the first letter to the end and add an ay
# If word does not begin with consonant, ignore
# If word is a joiner word (the, on, at, etc.) ignore
# Return new phrase
# Ask for new input or end


import sys

def pig_latin_translator(english):

    while True:    
        vowels = ('a','e','i','o','u')
        # joiners = ('the','and','not','is','or','at','to')
        words = english.split()
        new_words = []
        for word in words:
            if word[0] in vowels:
                new_words.append(word)
            # elif word in joiners:
            #     new_words.append(word)
            else:
                pig_letter = word[0]
                pig_word = word[1:] + pig_letter + 'ay'
                new_words.append(pig_word)
        sentence = " ".join(new_words)
        print("\n\n")
        print(sentence.lower())
        print("\n\n")
        break

def main():
    
    print('\n\nElcomeway To The Pig Latin Translator!\n')
    while True:    
        text = input("\n\nWrite your english sentence:\n")
        pig_latin_translator(text)
        try_again =  input("\n\nTry again? (Press ENTER else n to quit)\n")
        if try_again.lower() == "n":
            break


if __name__ == "__main__":
 main()


