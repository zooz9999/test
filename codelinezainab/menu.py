def print_pattern():
    n = int(input("Enter the number of rows for the  Pattern: "))
    if n <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(1, n + 1):
            print("*" * i)

def filter_numbers():
    numbers = input("Enter a list of whole numbers separated by spaces: ").split()
    filtered_numbers = []
    for num in numbers:
        if not (13 <= int(num) <= 19):
            filtered_numbers.append(num)
    print("Filtered list:", " ".join(filtered_numbers))

def display_help():
    print("Please select an Option:")
    print("1. Print Pattern")
    print("2. Filter Numbers")
    print("3. Help")
    print("4. Exit")

def print_help():
    print("---Help---")
    print("1. Print a specific pattern with 'n' rows.")
    print("2. Remove numbers between 13 and 19 from a list of whole numbers.")
    print("3. Display this help message.")
    print("4. Exit the program")

def main():
    while True:
        print("\nWelcome to the Menu-Based Program!")
        display_help()
        choice = input("Please select an Option:")

        if choice == '1':
            print_pattern()
        elif choice == '2':
            filter_numbers()
        elif choice == '3':
            print_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
