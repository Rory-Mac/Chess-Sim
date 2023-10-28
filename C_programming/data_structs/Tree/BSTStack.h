#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct Stack {
    int size;
    int top;
    struct BST *stackValues;
};

void push(struct Stack *stack, struct BST *value);

struct BST pop(struct Stack *stack);

struct BST peek(struct Stack *stack);

bool isEmpty(struct Stack *stack);

struct Stack *createStack(int size);