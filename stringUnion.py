#Max Low
#10-20-17
#stringUnion.py takes two words and then prints out all the apering letter each letter only once

def stringUnion(word1, word2):
    letters = ''
    for ch in word1:
        if ch not in letters:
            print(ch)
            letters = letters + ch
    for ch in word2: 
        if ch not in letters:
            print(ch)
            letters = letters + ch
        print(ch)
    
    print(letters)
    
    
stringUnion('mississippi','pennsylvania')

