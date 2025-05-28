import random

def jacobi_symbol(a, n):
    """Compute the Jacobi symbol (a/n)."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer.")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        a, n = n, a  # Swap
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0

def solovay_strassen(n, k=5):
    """Perform the Solovay-Strassen primality test on n."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = jacobi_symbol(a, n)
        if x == 0 or pow(a, (n - 1) // 2, n) != (x % n):
            return False
    return True

# Example usage
if __name__ == "__main__":
    num = 561 # Change this number to test other values
    if solovay_strassen(num):
        print(f"{num} is probably prime.")
    else:
        print(f"{num} is composite.")
