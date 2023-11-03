#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct Stack {
    int size;
    int top;
    int *stackValues;
};

void push(struct Stack *stack, int value);

int pop(struct Stack *stack);

int peek(struct Stack *stack);

bool isEmpty(struct Stack *stack);

struct Stack *createStack(int size);