def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0;
    for a in aDict.keys():
        result += len(aDict[a])

    return result

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = {};
    for a in aDict.keys():
        result[a] = (len(aDict[a]));

    max = 0;
    for b in result:
        if max < b:
            max = b;

    return max;

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals));