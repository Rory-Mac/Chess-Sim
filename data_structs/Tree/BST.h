#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct BST {
    int value;
    int size;
    struct BST *left;
    struct BST *right;
};

struct BST *CreateBST();

int InsertionTraversal(struct BST *tree, int value);

void InsertBSTNode(struct BST *tree, int value);

void RemoveBSTNode(struct BST *tree, int value);

void InorderPrint(struct BST *tree);

void PreorderPrint(struct BST *tree);

void PostorderPrint(struct BST *tree);

bool SearchTree(struct BST *tree, int value);

void ReverseBST(struct BST *tree);

int isBalanced(struct BST *tree, bool *balanced);

void InorderTraverse(struct BST *tree, int *treeValues);

void binarySearchInsert(struct BST *tree, int *values, int lo, int hi);

int BalanceBST(struct BST *tree);

int BSTinterface(int argc, char *argv[]);