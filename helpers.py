from tqdm import tqdm

def Eratosthenes_Sieve(max_val: int) -> set:
    prime_flags = [True] * max_val
    prime_flags[0] = False
    prime_flags[1] = False

    primes = set()

    for cur in range(max_val):
        if cur == False:
            continue

        primes.add(cur)

        for i in range(cur *2, max_val, cur):
            prime_flags[i] = False

    return primes