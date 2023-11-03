/*
            (x,y)
x ^= y      (x ^ y, y)
y ^= x      (x ^ y, y ^ (x ^ y)) = (x ^ y, x)
x ^= y      (x ^ y ^ x, x) = (y, x)

0101 (x)
0011 (y)
0110 (x ^= y)
0101 (y ^= x)
0011 (x ^=  y)
0011 (x)
0101 (y)

010010100101010 (x)
101010101010101 (y)
111000001111111 (x ^= y)
010010100101010 (y ^= x)
101010101010101 (x ^= y)
101010101010101 (x)
010010100101010 (y)

*/
#include <stdio.h>
#include <stdlib.h>

int main() {
    int x, y;
    while (1) {
        printf("Enter x y: ");
        scanf("%d %d", &x, &y);
        x ^= y;
        y ^= x;
        x ^= y;
        printf("%d %d\n", x, y);
    }
    return 0; 
}