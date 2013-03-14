def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    if len(str1) != 0 and len(str2) != 0:
        if str1[0] == str2[len(str2) - 1]:
            return semordnilap(str1[1:], str2[0:-1])
        else:
            return False;
    elif len(str1) == len(str2):
        return True;
    else:
        return False;

print(semordnilapWrapper('rats live on', 'no evil star'));
