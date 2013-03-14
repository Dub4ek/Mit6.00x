from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n, second = False):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """

    currentResult = 0;
    maxResult = 0;
    currentWord = '';

    for word in wordList:
        validationFlag = _isValidWord(word, hand, wordList);
        if validationFlag == True:
            currentResult = getWordScore(word, n);

        if currentResult > maxResult:
            maxResult = currentResult;
            currentWord = word;

    if maxResult > 0:
        return currentWord;
    else:
        return None;

def _isValidWord(word, hand, wordList):
    count = 0;
    currentHand = hand.copy();
    if word:
        for a in word:
            if a in currentHand and currentHand[a] != 0:
                count += 1;

                if currentHand[a] != 2:
                    del currentHand[a];

        if count == len(word):
            return True;
        else:
            return False;
    else:
        return False;

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    allPoints = 0;
    result = True;

    while result:
        print hand
        print 'Current hand:',displayHand(hand)
        currentWord = compChooseWord(hand, wordList, n);
        validationFlag = _isValidWord(currentWord, hand, wordList);

        if validationFlag == False:
            print 'Total score: ' + str(allPoints)  + ' points.';
            break;
        else:
            wordPoints = getWordScore(currentWord, n);
            allPoints += wordPoints;
            hand = updateHand(hand, currentWord);
            k = calculateHandlen(hand);

            if k == 0:
                print '"' + currentWord + '" earned ' + str(wordPoints) + ' points. Total: ' + str(allPoints);
                print 'Total score: ' + str(allPoints)  + ' points.';
                break;
            else:
                print '"' + currentWord + '" earned ' + str(wordPoints) + ' points. Total: ' + str(allPoints);



#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

#print compChooseWord({'a': 2, 'e': 2, 'i': 2, 't': 2}, wordList, 4);
print compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)

