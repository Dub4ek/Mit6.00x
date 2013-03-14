# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#


import string;

def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) > 0:
        return aStr[-1:] + str(reverseString(aStr[:-1]))
    else:
        return aStr[-1:]

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """

    if len(x) > 1 and len(word) > 1:
       if x[0] in word:
           return x_ian(x[1:], word[word.find(x[0]):])
       else:
        return False;
    elif x in word:
        return True;
    elif len(x) == 0:
        return True;
    else:
        return False;

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) > 0:
        currentLength = findSum(text, lineLength);
        return text[:currentLength] + '\n' + str(insertNewlines(text[currentLength:], lineLength));
    else:
        return ''



def findSum(text, lineLength):
    result = text[:lineLength];

    if result[-1:] == ' ' or result[-1:] == '.' or len(text) <= lineLength:
        return lineLength
    else:
        return findSum(text, lineLength + 1)


print insertNewlines('sdbfteyz dbi zoluqj fytzsl blopys tvflozhx rnecjpw bopau jyrg baxumsrd ljy zdocj wjb wztp zdgv adgukn xpwoqce dpzgkna pvhwza rbqpztly', 26)