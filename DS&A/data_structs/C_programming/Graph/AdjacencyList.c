#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include "AdjacencyList.h"

AdjacencyListNode *CreateAdjacencyListNode(int value) {
    AdjacencyListNode *newNode = malloc(sizeof(AdjacencyListNode));
    newNode->value = value;
    newNode->next = NULL;
    return newNode;
}

AdjacencyList *createAdjacencyList() {
    AdjacencyList *newList = malloc(sizeof(AdjacencyList));
    newList->size = 0;
    newList->head = NULL;
    newList->tail = NULL;
    return newList;
}

void AddAdjacencyListNode(AdjacencyList *list, int value, int nodeIndex) {
    if (nodeIndex > list->size + 1) {
        printf("Index out of bounds\n");
        return;
    }
    AdjacencyListNode *newNode = CreateAdjacencyListNode(value);
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
    AdjacencyListNode *curr = list->head;
    AdjacencyListNode *prev = list->head;
    for (int i = 1; i < nodeIndex; i++) {
        prev = curr;
        curr = curr->next;
    }
    prev->next = newNode;
    newNode->next = curr;
}

void RemoveAdjacencyListNode(AdjacencyList *list, int nodeIndex) {
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
    AdjacencyListNode *curr = list->head;
    AdjacencyListNode *prev = list->head;
    for (int i = 1; i < nodeIndex; i++) {
        prev = curr;
        curr = curr->next;
    }
    prev->next = curr->next;
    list->size--;
    free(curr);
}

void ReverseAdjacencyList(AdjacencyList *list) {
    AdjacencyListNode *prev = NULL;
    AdjacencyListNode *curr = list->head;
    AdjacencyListNode *next = list->head;
    list->tail = list->head;
    while (next != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    list->head = prev;
}

void PrintAdjacencyList(AdjacencyList *list, int nodeIndex) {
    AdjacencyListNode *curr = list->head;
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