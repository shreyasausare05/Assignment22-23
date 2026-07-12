from multiprocessing import Pool
import os

def even(no):
    print("PID of ",no, ":", os.getpid())
    count = 0
    for i in range(2, no + 1, 2):
        count += 1
    return count

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    with Pool() as pool:
        results = pool.map(even, number)

        print("Count of even numbers up to each number:", results)

if __name__ == "__main__":
    main()