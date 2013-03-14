def f(n):
    """
    n: integer, n >= 0.
    """
    if n == 0:
        return 1
    else:
        return n * f(n-1)

print(f(1));

def fib(a):
    if a == 0:
        return 1;
    else