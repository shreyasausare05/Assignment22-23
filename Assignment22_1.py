from multiprocessing import Pool

def sumsquare(no):
    sum = 0
    for i in range(1,no+1):
        sum += i*i
    return sum

def main():
    number = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Input numbers:", number)

    with Pool() as pool:
        results = pool.map(sumsquare, number)

        print("Sum of squares for each number:", results)

if __name__ == "__main__":
    main()