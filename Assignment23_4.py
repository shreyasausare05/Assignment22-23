from multiprocessing import Pool
import os

from Assignment23_3 import even

def odd(no):
    print("PID of ",no, ":", os.getpid())
    count = 0
    for i in range(1, no + 1, 2):
        count += 1
    return count

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    with Pool() as pool:
        results = pool.map(odd, number)

        print("Count of odd numbers up to each number:", results)

if __name__ == "__main__":
    main()