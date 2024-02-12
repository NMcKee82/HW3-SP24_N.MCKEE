import math

def calculate_gamma_function(alpha):
    """
    Calculate the gamma function value for a given alpha.

    Parameters:
        alpha (float): The input value for the gamma function.

    Returns:
        float: The result of the gamma function evaluation.
    """
    return math.gamma(alpha)

def calculate_Km(m):
    """
    Calculate the value of Km for a given degrees of freedom.

    Parameters:
        m (int): Degrees of freedom.

    Returns:
        float: The value of Km.
    """
    numerator = calculate_gamma_function((1/2)*m + (1/2))
    denominator = math.sqrt(m * math.pi) * calculate_gamma_function (0.5 * m)
    return numerator / denominator

def calculate_t_distribution(df, z):
    """
    Calculate the t-distribution function value for a given degrees of freedom and z-value.

    Parameters:
        df (int): Degrees of freedom.
        z (float): The z-value.

    Returns:
        float: The t-distribution function value.
    """
    m = df
    Km = calculate_Km(m)
    return Km * (1 + (z ** 2 / m)) ** (-(m + 1) / 2)

def main():
    degrees_of_freedom = [7, 11, 15]
    z_values = [0.00, 0.55, 1.41]

    for df in degrees_of_freedom:
        print(f"Degrees of Freedom: {df}")
        for z in z_values:
            try:
                t_distribution = calculate_t_distribution(df, z)
                print(f"Degrees of Freedom: {df}, z-value: {z}, Probability: {t_distribution}")
            except Exception as e:
                print(f"Error occurred for z={z}: {e}")

if __name__ == "__main__":
    main()
