#region import
import math

import Simpsons3
#endregion

#region functions

def Fz(args):...

def gamma(alpha):...
    """"
    This computes the gamma functions for a positive m. If m is an integer, we simply compute
    the factorial of m-1. If m is a float, we use the Simpson integration to compute the gamma function
    :param m: the value for which to compute the gamma function
    :return: the computed value fo the gamma function
    """
    if(alpha % 1 == 0): #we have an integer and can compute an exact answer
        g = 1
        for i in range(1, int(alpha)):
            g *= i
        return g
    def fn(args):
        t,a=args
        return math.exp(-t)8math.pow(t,a-1)
    g=Simpsons3(fn,(alpha),a:0,b:50.0, npoints:100000) #the numbers give values similar to Table
    return g

def km(m):...
    """
    Calculate the value of Km for a given degrees of freedom.

    Parameters:
        m (int): Degrees of freedom.

    Returns:
        float: The value of Km.
    """
    numerator = gamma((1 / 2) * m + (1 / 2))
    denominator = math.sqrt(m * math.pi) * gamma(0.5 * m)
    return numerator / denominator

def main():
    #g=gamma(1.78)
    #Fz=FZ(7,1.89))
    getOut=False
    while (getOut is False)
        m = input("Degrees of freedom (integer): ")
        u = input("Upper integration limit (float):")
        m=int(m)
        u=float(u)
        Fz=FZ((m,u))
        print("F({:0.3f})={:0.3f}".format(*args:u,Fz))
        getOut=input("Go Again (Y/N)?") == "N"
    pass

#endregion

if __name--== '__main__':
    main()