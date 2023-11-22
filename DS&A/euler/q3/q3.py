# pre-compute prime numbers
def sieve_of_eratosthenes(n) -> [int]:
    is_prime = [True for _ in range(n)]
    is_prime[0] = False
    is_prime[n - 1] = False
    for x in range(1, n):
        if not is_prime[x]: continue
        for kx in range((x + 1) * 2, n, x + 1):
            is_prime[kx - 1] = False
    discovered_primes = []
    for i in range(n):
        if is_prime[i]:
            discovered_primes.append(i + 1)
    return discovered_primes

# find the prime factors of a given integer
def prime_factors(n) -> [int]:
    primes = sieve_of_eratosthenes(10000)
    if n in primes: return [n]
    prime_factors = []
    while n not in primes:
        prime_factor_discovered = False
        for prime in primes:
            if n % prime == 0:
                prime_factors.append(prime)
                n /= prime
                prime_factor_discovered = True
                break
        if not prime_factor_discovered:
            print("More primes need to be computed to determine prime factorisation")
            break
    prime_factors.append(int(n))
    return prime_factors

def largest_prime_factor(n) -> int:
    return (max(prime_factors(n)))

if __name__ == "__main__":
    while (True):
        input_words = input("Input command: ").split()
        input_command = input_words[0]
        if len(input_words) > 1:
            input_value = int(input_words[1])
        if input_command == "help":
            print("\thelp : list valid commands")
            print("\tdiscover [n] : discover primes less than n using sieve of eratosthenes")
            print("\tpfactor [value] : determine the prime factors of [value]")
            print("\tgpfactor [value] : determine the greatest prime factor of [value]")
            print("\texit : exit interface")
        elif input_command == "discover":
            for prime in sieve_of_eratosthenes(input_value):
                print(f"{prime} ", end="")
            print()
        elif input_command == "pfactor":
            for prime_factor in prime_factors(input_value):
                print(f"{prime_factor} ", end="")
            print()
        elif input_command == "gpfactor":
            print(largest_prime_factor(input_value))
        elif input_command == "exit":
            break
        else:
            print("Unknown command, type 'help' to print command options")