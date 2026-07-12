from multiprocessing import Pool

def prime(no):
    if no < 2:
        return False
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            return False
    return True

def count_primes(no):
    count = 0
    for i in range(2, no + 1):
        if prime(i):
            count += 1
    return count

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    with Pool() as pool:
        results = pool.map(count_primes, number)

        print("Count of prime numbers up to each number:", results)

if __name__ == "__main__":
    main()