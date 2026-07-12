from multiprocessing import Pool
import os


def factorial(no):
    print("PID of ", no, ":", os.getpid())
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i
    return fact

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    with Pool() as pool:
        results = pool.map(factorial, number)

        print("Factorial for each number:", results)

if __name__ == "__main__":
    main()