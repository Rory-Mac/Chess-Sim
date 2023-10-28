#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "BSTStack.h"
#include "BST.h"

void push(struct Stack *stack, struct BST *tree) {
    if (stack->top == stack->size - 1) {
        printf("Stack full\n");
        return;
    }
    stack->top += 1;
    stack->stackValues[stack->top] = tree;
}

struct BST pop(struct Stack *stack) {
    if (stack->top == -1) {
        printf("Stack empty\n");
    }
    struct BST stackValue = stack->stackValues[stack->top];
    stack->top--;
    return stackValue;
}

struct BST peek(struct Stack *stack) {
    return stack->stackValues[stack->top];    
}

bool isEmpty(struct Stack *stack) {
    return stack->top == -1;
}

struct Stack *createStack(int size) {
    struct Stack *stack = malloc(sizeof(struct Stack));
    stack->size = size;
    stack->top = -1;
    stack->stackValues = malloc(size * sizeof(struct BST));
}