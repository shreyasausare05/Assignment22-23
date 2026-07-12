from multiprocessing import Pool
import time

def sum(no):
    sum = 0
    for i in range(1, no + 1):
        sum += i ** 5

    return sum

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    start_time = time.time()

    with Pool() as pool:
        results = pool.map(sum, number)

    end_time = time.time()

    print("Sum of fifth powers for each number:", results)
    print("Execution time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()