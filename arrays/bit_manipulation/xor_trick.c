int XOR_trick(n) {
    int x = n % 4;
    if (x == 0) {
        return n;
    } else if (x == 1) {

    } else if (x == 2) {

    } else if (x == 3) {

    }

}

int main() {
    int n;
    scanf("%d", &n);
    int result = XOR_trick(n);
    printf("Result: %d", result);
    return 0;
}

/*
a^0 = a
a^1 = !a
a^a = 0

a^b^c^d^a^b^c^d^a^b^c
a^a^b^b^c^c^d^d^a^b^c
a^b^c

1^2^3^4^5^6^7^8
(1^5)^(2^6)^(3^7)^(4^8)

x % 4 == 1
0001
0101
1001
1101
x % 4 == 2
0010
0110
1010
1110
x % 4 == 3
0011
0111
1011
1111
x % 4 == 0
0100
1000
1010
*/