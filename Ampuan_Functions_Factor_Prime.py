def smallest_factor(n):
    """Find the smallest factor of a given number."""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers_in_range(start, end):
    """Generate the prime numbers within the specified range."""
    prime_num = [num for num in range(start, end + 1) if is_prime(num)]
    return prime_num


while True:
    print("1. Find the smallest factor of a number")
    print("2. Find the prime numbers of range")
    print()
    choice = int(input("Select between 1 or 2: "))

    if choice == 1:
        number = int(input("Enter a number: "))
        result = smallest_factor(number)
        print("The smallest factor of", number, "is:", result)
        print()

    elif choice == 2:
        start_range = int(input("Enter the range (start): "))
        end_range = int(input("Enter the range (end): "))
        primes_in_range = prime_numbers_in_range(start_range, end_range)
        print("Prime numbers from", start_range, "to", end_range, "is/are:", primes_in_range)
        print()
    elif choice == 0:
        print("Invalid. Program terminated.")
        break

    else:
        print("Invalid. Please select between 1 or 2 only.")
        print()
