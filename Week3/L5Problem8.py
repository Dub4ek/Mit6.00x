def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    print(aStr + ' __ ' + char);
    if aStr == '':
        return False;
    elif len(aStr) == 1:
        if char == aStr:
            return True;
        else:
            return False;
    elif char > aStr[len(aStr) / 2]:
        return isIn(char, aStr[len(aStr) / 2:len(aStr)]);
    elif char < aStr[len(aStr) / 2]:
        return isIn(char, aStr[0:len(aStr) / 2]);
    elif char == aStr[len(aStr) / 2]:
        return True;


print(isIn('f', 'abcdef'))
