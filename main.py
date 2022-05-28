# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input('Enter word here: ')
    print(word)
    anagram = input('Enter anagram here: ')
    print(anagram)
    if(sorted(word) == sorted(anagram)):
        return True
    else:
        return False

find_anagram('word', 'anagram')
    

