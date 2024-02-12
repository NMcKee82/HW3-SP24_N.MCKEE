import math

def calculate_Fz(z, df):
    def f(u):
        return math.exp(-0.5 * u**2) / math.sqrt(2 * math.pi)

    def calculate_Km(m):
        numerator = math.gamma((m + 1) / 2)
        denominator = math.sqrt(m * math.pi) * math.gamma(m / 2)
        return numerator / denominator

    Km = calculate_Km(df)
    Fz = math.exp(-z**2 / 2) * (1 + (z**2 / df))**(-(df + 1) / 2) / (math.sqrt(2 * math.pi) * Km)
    return Fz

def main():
    df = int(input("Enter the degrees of freedom: "))
    z_values = []
    for i in range(3):
        z_values.append(float(input(f"Enter the value of upper integration {i+1}: ")))

    print(f"\nDegrees of Freedom: {df}")
    for z in z_values:
        probability = calculate_Fz(z, df)
        print(f"Probability for z={z}: {probability}")

if __name__ == "__main__":
    main()
