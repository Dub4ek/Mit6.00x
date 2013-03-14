def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    currentString = string.ascii_lowercase;

    for a in lettersGuessed:
        if currentString.index(a) != -1:
            currentString = currentString.replace(a,'');

    return currentString
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's'];
print getAvailableLetters(lettersGuessed)
