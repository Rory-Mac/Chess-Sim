#include <stdlib.h>
#include <stdbool.h>

struct Stack {
    int size;
    int top;
    int *stackValues;
} typedef Stack;

Stack *createStack(int stackSize);

void push(Stack *stack, int value);

int pop(Stack *stack);

bool isEmpty(Stack *stack);

bool isFull(Stack *stack);