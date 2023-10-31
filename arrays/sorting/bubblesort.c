#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

void bubbleSort(int *elems, int size) {
    bool sorted = true;
    while (true) {
        for (int i = 0; i < size - 1; i++) {
            if (elems[i] > elems[i + 1]) {
                int temp = elems[i];
                elems[i] = elems[i + 1];
                elems[i + 1] = temp;
                sorted = false;
            }
        }
        if (sorted) break;
        sorted = true;
    }
}

int main(int argc, char *argv[]) {
    int size = 100;
    int elems[size];
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        elems[i] = rand();
    }
    bubbleSort(elems, size);
    bool arraySorted = true;
    for (int i = 0; i < size - 1; i++) {
        if (elems[i] > elems[i+1]) {
            arraySorted = false;
        }
    }
    if (arraySorted) {
        printf("Array sorted succesfully\n");
        for (int i = 0; i < size; i++) {
            printf("%d ", elems[i]);
        }
    } else {
        printf("Array sort failed\n");
    }
}