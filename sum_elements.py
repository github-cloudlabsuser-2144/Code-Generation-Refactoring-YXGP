# A refactored example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles basic error cases.

MAX = 100

def calculate_sum(arr):
    """Calculate the sum of a list of integers."""
    return sum(arr)

def get_number_of_elements():
    """Prompt the user for the number of elements to sum."""
    while True:
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if 1 <= n <= MAX:
                return n
            else:
                print(f"Invalid input. Please provide a number between 1 and {MAX}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    """Prompt the user to input n integers."""
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        while True:
            try:
                num = int(input())
                arr.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return arr

def main():
    """Main function to execute the program."""
    try:
        n = get_number_of_elements()
        arr = get_elements(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
