print('Problem 3.10')
#input sring s if no vowel in input print true else false
def noVowel(s):
    if s in 'aeiouAEIOU':
        return 'false'
    else:
        return 'true'
s= input('Enter a string to check whether it is valid or not: ')
print(noVowel(s))
