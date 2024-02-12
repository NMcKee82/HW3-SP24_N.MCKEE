import math
import Simpsons3

def Fz(args):
    """
    Calculate the F(z) function for a given degrees of freedom (m) and upper limit of integration (u).

    Parameters:
        args (tuple): A tuple containing the degrees of freedom (m) and upper limit of integration (u).

    Returns:
        float: The value of F(z) for the given degrees of freedom and upper limit of integration.
    """
    m, u = args
    k_m = km(m)
    return 1 - (1 - Fz_partial(u, m)) * k_m

def Fz_partial(u, m):
    """
    Calculate the partial value of F(z) for a given upper limit of integration (u) and degrees of freedom (m).

    Parameters:
        u (float): The upper limit of integration.
        m (int): Degrees of freedom.

    Returns:
        float: The partial value of F(z) for the given upper limit of integration and degrees of freedom.
    """
    return math.sqrt(math.pi) * Simpson2(fz_partial_integrand, (m, u), 0, 1) / 2

def fz_partial_integrand(args):
    """
    Calculate the integrand for the partial F(z) calculation.

    Parameters:
        args (tuple): A tuple containing the degrees of freedom (m) and upper limit of integration (u).

    Returns:
        float: The value of the integrand at the given point.
    """
    m, u = args
    t, _ = args
    return math.exp(-t) * math.pow(t, (m - 1) / 2)

def gamma(alpha):
    """
    Compute the gamma function for a positive m. If m is an integer, compute the factorial of m-1.
    If m is a float, use Simpson integration to compute the gamma function.

    Parameters:
        alpha (float): The value for which to compute the gamma function.

    Returns:
        float: The computed value of the gamma function.
    """
    if alpha % 1 == 0:  # we have an integer and can compute an exact answer
        g = 1
        for i in range(1, int(alpha)):
            g *= i
        return g

    def fn(t, a):
        return math.exp(-t) * math.pow(t, a - 1)

    g = Simpson2(fn, (alpha, ), 0, 50.0, npoints=100000)
    return g

def km(m):
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
    get_out = False
    while not get_out:
        m = int(input("Degrees of freedom (integer): "))
        u = float(input("Upper integration limit (float): "))
        F_z = Fz((m, u))
        print("F({:.3f}) = {:.3f}".format(u, F_z))
        get_out = input("Go Again (Y/N)? ") == "N"

if __name__ == '__main__':
    main()
