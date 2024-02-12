def Simpson2(fcn, args, a, b, npoints=21):
    '''
    This uses the simpson 1/3 rule for numerical integration which uses
    See 3013 Text Book page 831-832
    The panel size is: dX=abs(a-b)/(2*npoints)
    The integral is found by: I=dX/3*(fcn(0)+fcn(npoints)+4*sum(fcn(j), 1 to n-1, odd)+28(fcn(j)
    :param fcn: the callback function. the function of x to integrate
    :param args: contains parameter for the function in tuple format. fcn is responsible for on
    :param a: left limit of integration (check a<b)
    :param b: right limit of integration (check a<b)
    :param npoints: number of integration
    :return: the value of the integration of fcn(x) between a,b
    '''
    area = 0  # initial value for the integral
    m = npoints  # staying consistent with the book nomenclature
    n = 2 * m  # ensure an even number of panels
    # if a,b are passed wrong, this checks to put them in correct order
    xL = min(a, b)  # lower limit of integration
    xR = max(a, b)  # upper limit of integration

    if xL == xR:
        return 0  # nothing to compute, return 0

    h = (xR - xL) / (2 * m)  # calculate panel width
    x = xL
    area = fcn(xL, *args) + fcn(xR, *args)  # first calculate f(x) at xL and xR

    for j in range(1, 2 * m):  # update counts from 1 to 2*m-1
        x = j * h + xL  # update the x position for evaluating the function
        if not j % 2 == 0:  # the odds
            area += 4 * fcn(x, *args)
        else:  # the evens
            area += 2 * fcn(x, *args)
    return (h / 3) * area  # finally, returns the value for the integral
