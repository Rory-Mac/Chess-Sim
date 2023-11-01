#include <stdlib.h>
#include <stdbool.h>
#include "Stack.h"

Stack *createStack(int stackSize) {
    Stack *newStack = (Stack *)malloc(sizeof(Stack)); 
    newStack->top = -1;
    newStack->size = stackSize;
    newStack->stackValues = (int *)malloc(stackSize * sizeof(int));
    return newStack;
}

void freeStack(Stack *stack) {
    free(stack->stackValues);
    free(stack);
}

void push(Stack *stack, int value) {
    if (isFull(stack)) return;
    stack->top += 1;
    stack->stackValues[stack->top] = value;
}

int pop(Stack *stack) {
    if (isEmpty(stack)) return -1;
    int stackValue = stack->stackValues[stack->top];
    stack->top -= 1;
    return stackValue;
}

bool isEmpty(Stack *stack) {
    return stack->top == -1;
}

bool isFull(Stack *stack) {
    return stack->top == stack->size;
}