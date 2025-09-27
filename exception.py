age_input = input("Enter your age: ")

try:
    age = int(age_input)
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Your age is {age}.")
except ValueError as ve:
    print("Invalid age:", ve)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    result = "5" + 3
except TypeError:
    print("Error: Cannot add string and integer.")

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: List index out of range.")

try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError:
    print("Error: Key not found in dictionary.")

try:
    number = int("hello")
except ValueError:
    print("Error: Cannot convert string to integer.")

num_input = input("Enter a positive number: ")

try:
    num = int(num_input)
    assert num > 0, "Number must be positive."
    print(f"You entered {num}, which is valid.")
except AssertionError as ae:
    print("Assertion failed:", ae)
except ValueError:
    print("Error: Please enter a valid integer.")

def process_numbers(numbers):
    try:
        if not numbers:
            raise ValueError("Empty list detected.")
        total = sum(numbers)
        print(f"Sum of numbers: {total}")
    except ValueError:
        print("List cannot be empty!")

process_numbers([])
process_numbers([1, 2, 3, 4])