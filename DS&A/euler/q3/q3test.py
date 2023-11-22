import q3
prime_factors = q3.prime_factors(87)
assert len(prime_factors) == 2
assert prime_factors[0] == 3
assert prime_factors[1] == 29
assert q3.largest_prime_factor(87) == 29
prime_factors = q3.prime_factors(54)
assert len(prime_factors) == 4
assert prime_factors[0] == 2
assert prime_factors[1] == 3
assert prime_factors[2] == 3
assert prime_factors[3] == 3
assert q3.largest_prime_factor(54) == 3
prime_factors = q3.prime_factors(600851475143)
assert len(prime_factors) == 4
assert prime_factors[0] == 71
assert prime_factors[1] == 839
assert prime_factors[2] == 1471
assert prime_factors[3] == 6857
assert q3.largest_prime_factor(600851475143) == 6857