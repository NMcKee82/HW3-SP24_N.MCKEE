import math


def gamma_function(alpha):
    """
    Compute the gamma function using the math.gamma function.

    Parameters:
        alpha (float): The parameter of the gamma function.

    Returns:
        float: The value of the gamma function at alpha.
    """
    result = math.gamma(alpha)
    print(f"Gamma Function Result: {result}")  # Debug
    return result


def calculate_Km(m):
    """
    Calculate the normalization constant K_m for the t-distribution.

    Parameters:
        m (float): The parameter related to the degrees of freedom.

    Returns:
        float: The value of the normalization constant K_m.
    """
    numerator = gamma_function(0.5 * m + 0.5)
    denominator = math.sqrt(m * math.pi) * gamma_function(0.5 * m) * (0.5 * m)

    print(f"Numerator: {numerator}, Denominator: {denominator}")  # Debug

    # Avoid division by zero
    if denominator == 0:
        return float('inf')  # Return infinity to indicate an error

    return numerator / denominator


def integrand(u, m):
    """
    Define the integrand for the cumulative distribution function (CDF) of the t-distribution.

    Parameters:
        u (float): The variable of integration.
        m (float): The parameter related to the degrees of freedom.

    Returns:
        float: The value of the integrand at u.
    """
    return (1 + u ** 2 / m) ** ((m + 1) / 2)


def calculate_probability(degrees_of_freedom, z_value):
    """
    Calculate the probability using the cumulative distribution function (CDF) of the t-distribution.

    Parameters:
        degrees_of_freedom (int): The degrees of freedom.
        z_value (float): The value at which to evaluate the probability.

    Returns:
        float: The probability.
    """
    m = degrees_of_freedom / 2
    Km = calculate_Km(m)

    print(f"Degrees of Freedom: {degrees_of_freedom}, z-value: {z_value}, Km: {Km}")  # Debug

    # Avoid division by zero
    if Km == float('inf'):
        return float('nan')  # Return nan to indicate an error

    def integrate(a, b, N):
        """
        Numerical integration using the trapezoidal rule.

        Parameters:
            a (float): Lower limit of integration.
            b (float): Upper limit of integration.
            N (int): Number of intervals for integration.

        Returns:
            float: The approximate value of the integral.
        """
        h = (b - a) / N
        sum_area = 0.5 * (integrand(a, m) + integrand(b, m))
        for i in range(1, N):
            sum_area += integrand(a + i * h, m)
        return h * sum_area

    try:
        result = integrate(-float('inf'), z_value, 1000)
        probability = Km * result
    except Exception as e:
        print(f"Error occurred: {e}")
        probability = float('nan')  # Return nan to indicate an error

    return probability


def main():
    """
    Main function to prompt user input and calculate the probability.
    """
    # Prompt the user to enter values for degrees of freedom
    degrees_of_freedom_values = [int(input("Enter degrees of freedom (e.g., 7, 11, 15): ")) for _ in range(3)]

    # Prompt the user to enter values for z
    z_values = [float(input(f"Enter z value {i + 1}: ")) for i in range(3)]

    # Iterate over degrees of freedom and z-values
    for df in degrees_of_freedom_values:
        print(f"\nDegrees of Freedom: {df}")
        for z in z_values:
            probability = calculate_probability(df, z)
            if math.isnan(probability):
                print(f"Error occurred for z={z}")
            else:
                print(f"Probability for z={z}: {probability}")


if __name__ == "__main__":
    main()
