def print_multiplication_table(n):
    """Prints a multiplication table for numbers 1 to n."""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} * {j} = {i * j}", end='\t')
        print()

def main():
    n = 10
    print_multiplication_table(n)

if __name__ == "__main__":
    main()
