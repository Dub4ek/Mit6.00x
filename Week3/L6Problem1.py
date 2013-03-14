def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    test = ();
    for a in range(len(aTup)):
        if a % 2 == 0:
            test += (aTup[a],);

    return test
print(oddTuples((1, 'a', 4, 't', 5)));


listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
listA.sort();
listA.insert(0, 100);
listA.remove(3);
listA.append(7)
listA = listA + listB;
listB.sort();
listB.pop();
listA.extend([4, 1, 6, 3, 4])
listA.pop(4)
listA.reverse()
print(listA);