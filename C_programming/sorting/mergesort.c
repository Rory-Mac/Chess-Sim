#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

void merge(int *elems, int lo, int mid, int hi) {
    int i, j, k;
    int l1 = mid - lo + 1;
    int l2 = hi - mid;
    int A[l1], B[l2];
    
        

}

void mergeSort(int *elems, int lo, int hi) {
    if (lo == hi) return;
    int mid = lo + (hi - lo) / 2;
    mergeSort(elems, lo, mid);
    mergeSort(elems, mid + 1, hi);
    merge(elems, lo, mid, hi);
}

int main(int argc, char *argv[]) {
    int size = 100;
    int elems[size];
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        elems[i] = rand();
    }
    mergeSort(elems, 0, size);
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