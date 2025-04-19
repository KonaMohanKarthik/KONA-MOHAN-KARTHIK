def count_multiples(numbers):
    counts = {i: 0 for i in range(1, 10)}
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                counts[i] += 1
    return counts

if __name__ == "__main__":
    try:
        user_input = input("Enter a list of integers separated by commas: ")
        numbers = list(map(int, user_input.split(',')))
        result = count_multiples(numbers)
        print("Dictionary Count of Multiples:")
        for k, v in result.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {e}")
