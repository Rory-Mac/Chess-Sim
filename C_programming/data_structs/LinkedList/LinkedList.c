#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

struct LinkedList {
    int size;
    struct LinkedListNode *head;
    struct LinkedListNode *tail;
};

struct LinkedListNode {
    int value;
    struct LinkedListNode *next;
};

struct LinkedListNode *CreateLinkedListNode(int value) {
    struct LinkedListNode *newNode = malloc(sizeof(struct LinkedListNode));
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

struct LinkedList *createLinkedList() {
    struct LinkedList *newList = malloc(sizeof(struct LinkedList));
    newList->size = 0;
    newList->head = NULL;
    newList->tail = NULL;
    return newList;
}

void AddLinkedListNode(struct LinkedList *list, int value, int nodeIndex) {
    if (nodeIndex > list->size + 1) {
        printf("Index out of bounds\n");
        return;
    }
    struct LinkedListNode *newNode = CreateLinkedListNode(value);
    list->size++;
    if (list->size == 0) {
        list->head = newNode;
        list->tail = newNode;
        return;
    }
    if (nodeIndex == 1) {
        newNode->next = list->head;
        list->head = newNode;
        return;
    } 
    struct LinkedListNode *curr = list->head;
    struct LinkedListNode *prev = list->head;
    for (int i = 1; i < nodeIndex; i++) {
        prev = curr;
        curr = curr->next;
    }
    prev->next = newNode;
    newNode->next = curr;
}

void RemoveLinkedListNode(struct LinkedList *list, int nodeIndex) {
    if (list->size == 0) return;
    if (list->size == 1) {
        free(list->head);
        list->head = NULL;
        list->tail = NULL;
        list->size--;
        return;
    }
    if (nodeIndex == 1) {
        free(list->head);
        list->head = list->head->next;
        list->size--;
        return; 
    }
    struct LinkedListNode *curr = list->head;
    struct LinkedListNode *prev = list->head;
    for (int i = 1; i < nodeIndex; i++) {
        prev = curr;
        curr = curr->next;
    }
    prev->next = curr->next;
    list->size--;
    free(curr);
}

void PrintLinkedList(struct LinkedList *list, int nodeIndex) {
    struct LinkedListNode *curr = list->head;
    if (list->size == 0) {
        printf("[]\n");
        return;
    }
    if (list->size == 1) {
        printf("[%d] -> NULL\n", curr->value);
        return;
    }
    while (curr->next != NULL) {
        printf("[%d] -> ", curr->value);
        curr = curr->next;
    }
    printf("[%d] -> ", curr->value);
    printf("NULL\n");
}

int main(int argc, char *argv[]) {
    struct LinkedList *list = createLinkedList();
    char command[255];
    int nodeValue;
    int nodeIndex;
    while (true) {
        printf("Input Instruction: ");
        scanf("%s", &command);
        if (strcmp(command, "help\0") == 0) {
            printf("\tadd [value] [index] : add node to linked list\n");
            printf("\tremove [index] : remove node from linked list\n");
            printf("\tprint : print linked list\n");
        } else if (strcmp(command, "add\0") == 0) {
            scanf("%d %d", &nodeValue, &nodeIndex);
            AddLinkedListNode(list, nodeValue, nodeIndex);
        } else if (strcmp(command, "remove\0") == 0) {
            scanf("%d", &nodeIndex);
            RemoveLinkedListNode(list, nodeIndex);
        } else if (strcmp(command, "print\0") == 0) {
            PrintLinkedList(list, nodeIndex);
        } else if (strcmp(command, "exit\0") == 0) {
            break;
        } else {
            printf("Input unknown, type 'help' for list of commands.\n");
        }
    }
    return 0;
}