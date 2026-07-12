from multiprocessing import Pool
import os

def sumeven(no):
    print("PID of ", no, ":", os.getpid())
    sum = 0
    for i in range(2, no + 1,2):
        sum += i
    return sum

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    with Pool() as pool:
        results = pool.map(sumeven, number)

        print("Sum of even numbers for each number:", results)

if __name__ == "__main__":
    main()