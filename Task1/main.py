class Calculator:
    def __init__(self):
        self.numbers = []

    def add(self):
        """Addition of numbers"""
        return sum(self.numbers)

    def subtract(self):
        """Subtraction of numbers"""
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        return result

    def multiply(self):
        """Multiplication of numbers"""
        result = 1
        for num in self.numbers:
            result *= num
        return result

    def divide(self):
        """Division of numbers"""
        result = self.numbers[0]
        for num in self.numbers[1:]:
            if num == 0:
                return "Error"
            result /= num
        return result

    def get_numbers(self):
        """Get user input for numbers"""
        print("Enter numbers one by one. Type 'stop' to finish entering numbers.")
        while True:
            user_input = input("Enter a number (or type 'stop' to finish): ").lower()
            if user_input == 'stop':
                break
            if user_input.replace('.', '', 1).isdigit():
                self.numbers.append(float(user_input))
            else:
                print("Invalid input. Please enter a number.")
        if len(self.numbers) == 0:
            print("No numbers entered. Exiting program.")
            return False
        return True

    def choose_operation(self):
        """Choose and perform an operation"""
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            print("Result:", self.add())
        elif choice == '2':
            print("Result:", self.subtract())
        elif choice == '3':
            print("Result:", self.multiply())
        elif choice == '4':
            print("Result:", self.divide())
        else:
            print("Invalid choice")


calc = Calculator()
if calc.get_numbers():
    calc.choose_operation()
