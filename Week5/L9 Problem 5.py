import string;

def hash(s):
    return string.ascii_lowercase.index(s[0])

print(hash('cat'));