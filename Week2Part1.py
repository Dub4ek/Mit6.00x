print('Please think of a number between 0 and 100!');
startDiapazon = 0;
endDiapazon = 100;
secretNum = 50;

currentInput = '';

while currentInput != 'c':
    print('Is your secret number ' + str(secretNum) + '?');

    currentInput = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ');

    if currentInput == 'l':
        startDiapazon = secretNum;
    elif currentInput == 'h':
        endDiapazon = secretNum;
    elif currentInput != 'c':
        print("Sorry, I did not understand your input.");

    if (endDiapazon - startDiapazon > 1):
        secretNum = (endDiapazon - startDiapazon) / 2 + startDiapazon;
    elif (startDiapazon == 0 and endDiapazon == 1):
        secretNum = startDiapazon;
    elif (startDiapazon == 99 and endDiapazon == 100):
        secretNum = endDiapazon;


print('Game over. Your secret number was:' + str(secretNum));

