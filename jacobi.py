import math

def quadratic_residues(p):
    qr = set()
    for i in range(1, p):
        qr.add(i**2%p)

    return qr

def quadratic_residues_with_prime(a, p):
    a = a%p
    ans = pow(a,(p-1)//2, p)

    if ans == 1:
        return 1
    else:
        return -1

def main():
    a = int(input("Enter a: "))
    p = int(input("Enter p: "))

    qr = quadratic_residues(p)
    print(f"qr is {qr}")

    ans = quadratic_residues_with_prime(a, p)
    print(f"ans is {ans}")

if __name__ == "__main__":
    main()
