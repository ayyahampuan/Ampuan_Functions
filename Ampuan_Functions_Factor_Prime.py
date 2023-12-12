def smallest(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n

def pri(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    prime_num = [num for num in range(start, end + 1) if pri(num)]
    return prime_num

while True:
    print("1. Find the smallest factor of a number")
    print("2. Find the prime numbers of range")
    print()
    choice = int(input("Select between 1 or 2: "))

    if choice == 1:
        num1 = int(input("Enter a number: "))
        res = smallest(num1)
        print("The smallest factor of", num1, "is:", res)
        print()

    elif choice == 2:
        start = int(input("Enter the range (start): "))
        end = int(input("Enter the range (end): "))
        primes = primes_in_range(start, end)
        print("The prime numbers from", start, "to", end, "is/are:", primes)
        print()

    elif choice == 0:
        print("Invalid. Program terminated.")
        break

    else:
        print("Invalid. Please select between 1 or 2 only.")
        print()
