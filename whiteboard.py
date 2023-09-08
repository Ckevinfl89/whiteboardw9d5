# Complete the function scramble(str1, str2) that returns true 
# if a portion of str1 characters can be rearranged to match str2,
# otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z)
# No punctuation or digits will be included.

# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False

def solution(str1, str2):
    if str2 == '':
        return True
    for letter in str2:
        if letter in str1:
            pass
        if letter not in str1:
            return False

    return True


def solution(str1, str2):
    dict = {}

    for letter in str1:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    
    for letter in str2:
        if letter not in dict:
            return False
        else:
            dict[letter] -= 1
            if dict[letter] < 0:
                return False
     
    return True