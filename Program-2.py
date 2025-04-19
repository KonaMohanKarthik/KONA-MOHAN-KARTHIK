def generate_odd_series(n: int):
    series = [2 * i + 1 for i in range(n)]
    return series

if __name__ == "__main__":
    try:
        a = int(input("Enter a positive integer: "))
        if a < 1:
            raise ValueError("Input must be a positive integer.")
        result = generate_odd_series(a)
        print("Output:", ', '.join(map(str, result)))
    except Exception as e:
        print(f"Error: {e}")
