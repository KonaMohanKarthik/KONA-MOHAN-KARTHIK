class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0.0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def calculate(self, a: float, b: float, operation: str) -> float:
        op = operation.lower()
        if op == "add":
            return self.add(a, b)
        elif op == "subtract":
            return self.subtract(a, b)
        elif op == "multiply":
            return self.multiply(a, b)
        elif op == "divide":
            return self.divide(a, b)
        else:
            raise ValueError(f"Unsupported operation: '{operation}'")

if __name__ == "__main__":
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        operation = input("Enter operation (add, subtract, multiply, divide): ")

        calc = Calculator()
        result = calc.calculate(a, b, operation)
        print(f"Result: {result}")

    except Exception as e:
        print(f"Error: {e}")
 