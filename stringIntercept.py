#Max Low
#10-20-17
#stringintercept.py takes two words and then prints out all the apering letter each letter only once

def stringUnion(word1, word2):
    letters1 = ''
    letters2 = ''
    letters3 = ''
    for ch in word1:
        if ch not in letters1:
            letters1 = letters1 + ch
    for ch in word2: 
        if ch not in letters2:
            letters2 = letters2 + ch
            
    for ch in letters1: 
        if ch in letters2:
            letters3 += ch
    
    return(letters3)
    
    
print(stringUnion('mississippi','pennsylvania'))

