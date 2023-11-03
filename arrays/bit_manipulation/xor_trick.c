/*
x ^ (x + 1) = 1 (if x is even)

0^1^2^3^4^5^6^7
(0^1)^(2^3)^(4^5)^(6^7)
1^1^1^1
0

0^1^2^3^4^5^6^7^n (n mod 4 == 0)
0^1^2^3^4^5^6^7^8^n (n mod 4 == 1)
0^1^2^3^4^5^6^7^8^9^n (n mod 4 == 2)
0^1^2^3^4^5^6^7^8^9^10^n (n mod 4 == 3)

0^n = n
0^1 = 1
0^1^n = n + 1 
0^1^1 = 0

*/
#include <stdio.h>

int XOR_trick(int n) {
    int x = n % 4;
    if (x == 0) {
        return n;
    } else if (x == 1) {
        return 1;
    } else if (x == 2) {
        return n + 1;
    } else if (x == 3) {
        return 0;
    }
}

int naive_approach(int n) {
    int result = 0;
    for (int i = 0; i <= n; i++) {
        result ^= i;
    }
    return result;
}

int main() {
    int n;
    while (1) {
        printf("Enter number: ");
        scanf("%d", &n);
        printf("%d %d\n", XOR_trick(n), naive_approach(n));
    }
    return 0;
}