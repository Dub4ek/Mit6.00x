"""
num = 3;
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val
"""

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

def foo(L):
    val = L[0]
    while (True):
        print 'a'
        val = L[val]


print foo(b)