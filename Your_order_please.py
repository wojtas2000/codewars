# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.
# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

import collections

def order(sentence):
    
    zdanie = sentence.split(' ')
    kolej = []
    slownik = {}
    for i in zdanie:
        for j in i:
            if j.isdigit():
                slownik[int(j)] = i
    if sentence == "":
        return ""
    slotnik2 = collections.OrderedDict(sorted(slownik.items()))

    wynik = []
    for k, v in slotnik2.items():
        wynik.append(v)
    return ' '.join(wynik)
