#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "Stack.h"

void push(struct Stack *stack, int value) {
    if (stack->top == stack->size - 1) {
        printf("Stack full\n");
        return;
    }
    stack->top += 1;
    stack->stackValues[stack->top] = value;
}

int pop(struct Stack *stack) {
    if (stack->top == -1) {
        printf("Stack empty\n");
        return -1;
    }
    int stackValue = stack->stackValues[stack->top];
    stack->top--;
    return stackValue;
}

int peek(struct Stack *stack) {
    return stack->stackValues[stack->top];    
}

bool isEmpty(struct Stack *stack) {
    return stack->top == -1;
}

struct Stack *createStack(int size) {
    struct Stack *stack = malloc(sizeof(struct Stack));
    stack->size = size;
    stack->top = -1;
    stack->stackValues = malloc(size * sizeof(int));
}

int stackInterface(int argc, char *argv[]) {
    struct Stack *stack = createStack(8);
    char command[255];
    int value;
    while (true) {
        printf("Input command: ");
        scanf("%s", &command);
        if (strcmp(command, "help\0") == 0) {
            printf("push [value]: pop a value onto the stack\n");
            printf("pop: pop a value from the stack\n");
            printf("peek: peek top of stack without removal\n");
            printf("isempty: check if stack is empty\n");
            printf("exit: exit command interface\n");
        } else if (strcmp(command, "push\0") == 0) {
            scanf("%d", &value);
            push(stack, value);
        } else if (strcmp(command, "pop\0") == 0) {
            printf("%d\n", pop(stack));
        } else if (strcmp(command, "peek\0") == 0) {
            printf("%d\n", peek(stack));
        } else if (strcmp(command, "isempty\0") == 0) {
            printf("%s", isEmpty(stack) ? "true\n" : "false\n");
        } else if (strcmp(command, "exit\0") == 0) {
            break;
        }
    }
    return 0;
}