#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

void merge(int *elems, int lo, int mid, int hi) {
    int i, j, k;
    int l1 = mid - lo + 1;
    int l2 = hi - mid;
    int A[l1], B[l2];
    for (i = 0; i < l1; i++) {
        A[i] = elems[lo + i];
    }
    for (j = 0; j < l2; j++) {
        B[j] = elems[mid + 1 + j];
    }
    i = 0;
    j = 0;
    k = lo;
    while (i < l1 && j < l2) {
        if (A[i] <= B[j]) {
            elems[k] = A[i];
            i++;
        } else {
            elems[k] = B[j];
            j++;
        }
        k++;
    }
    while (i < l1) {
        elems[k] = A[i];
        i++;
        k++;
    }
    while (j < l2) {
        elems[k] = B[j];
        j++;
        k++;
    }
}

void mergeSort(int *elems, int lo, int hi) {
    if (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        mergeSort(elems, lo, mid);
        mergeSort(elems, mid + 1, hi);
        merge(elems, lo, mid, hi);
    }
}

int main(int argc, char *argv[]) {
    int size = 10;
    int elems[size];
    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        elems[i] = rand();
    }
    mergeSort(elems, 0, size - 1);
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
        for (int i = 0; i < size; i++) {
            printf("%d ", elems[i]);
        }
    }
}