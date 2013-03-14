def f(x):
    import math
    return 60*math.e**(math.log(0.5)/55.6 * x)


def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    sum = 0;

    if step >= 1:
        while start < stop:
            sum += f(start)*step;
            start = start + step;
    else:
        while start < stop:
            sum += f(start)* step;
            start = start + step;

    return sum;


print(radiationExposure(600, 1200, 5))
