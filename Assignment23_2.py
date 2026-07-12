from multiprocessing import Pool
import os

def sumodd(no):
    print("PID of process calculating sum of odd numbers:", os.getpid())
    sum = 0
    for i in range(1, no + 1,2):
        sum += i
    return sum

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    with Pool() as pool:
        results = pool.map(sumodd, number)

        print("Sum of odd numbers for each number:", results)

if __name__ == "__main__":
    main()