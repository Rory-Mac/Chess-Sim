#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "BST.h"
#include "BSTStack.h"

struct BST *CreateBST() {
    struct BST *newTree = malloc(sizeof(struct BST));
    newTree->value = 0;
    newTree->left = NULL;
    newTree->right = NULL;
}

int InsertionTraversal(struct BST *tree, int value) {
    struct BST *curr = tree;
    if (tree->value > value) {
        if (tree->left == NULL) {
            struct BST *newTree = CreateBST();
            newTree->value = value;
            tree->left = newTree;
            return 0;
        }
        return InsertionTraversal(tree->left, value);
    } else if (tree->value < value) {
        if (tree->right == NULL) {
            struct BST *newTree = CreateBST();
            newTree->value = value;
            tree->right = newTree;
            return 0;
        }
        return InsertionTraversal(tree->right, value);
    }
    return -1;
}

void InsertBSTNode(struct BST *tree, int value) {
    if (InsertionTraversal(tree, value) == -1) {
        printf("Error: value already exists in BST\n");
        return;
    }
    tree->size++;
}

void RemoveBSTNode(struct BST *tree, int value) {
    if (tree == NULL || tree->left == NULL && tree->right == NULL) return;
    if (tree->left != NULL && tree->left->value == value) {
        struct BST *left_subtree = tree->left->left;
        struct BST *right_subtree = tree->left->right;
        free(tree->left);
        tree->left = right_subtree;
        struct BST *curr = right_subtree;
        while (curr->left != NULL) {
            curr = curr->left;
        }
        curr->left = left_subtree;
    } else if (tree->right != NULL && tree->right->value == value) {
        struct BST *left_subtree = tree->right->left;
        struct BST *right_subtree = tree->right->right;
        free(tree->right);
        tree->right = left_subtree;
        struct BST *curr = left_subtree;
        while (curr->right != NULL) {
            curr = curr->right;
        }
        curr->right = right_subtree;
    }
    RemoveBSTNode(tree->left, value);
    RemoveBSTNode(tree->right, value);
}

void InorderPrint(struct BST *tree) {
    if (tree == NULL) return;
    InorderPrint(tree->left);
    printf("%d", tree->value);
    InorderPrint(tree->right);
}

void PreorderPrint(struct BST *tree) {
    if (tree == NULL) return;
    printf("%d", tree->value);
    PreorderPrint(tree->left);
    PreorderPrint(tree->right);
}

void PostorderPrint(struct BST *tree) {
    if (tree == NULL) return;
    PostorderPrint(tree->left);
    PostorderPrint(tree->right);
    printf("%d", tree->value);
}

bool SearchTree(struct BST *tree, int value) {
    if (tree == NULL) return false;
    if (tree->value == value) return true;
    return SearchTree(tree->left, value) || SearchTree(tree->right, value);
}

void ReverseBST(struct BST *tree) {
    if (tree == NULL) return;
    ReverseBST(tree->left);
    ReverseBST(tree->right);
    struct BST *temp = tree->right;
    tree->left = temp;
    tree->right = tree->left;
}

int isBalanced(struct BST *tree, bool *balanced) {
    if (tree->left == NULL && tree->right == NULL) return 0;
    int depth_left = isBalanced(tree->left, balanced);
    int depth_right = isBalanced(tree->right, balanced);
    if (abs(depth_left - depth_right) > 1) {
        *balanced = true;
    }
    return depth_left > depth_right ? depth_left + 1 : depth_right + 1;
}

void InorderTraverse(struct BST *tree, int *treeValues) {
    struct Stack *stack = createStack(tree->size);
    struct BST *curr = tree;
    while (curr != NULL) {
        push(stack, curr);
        curr = curr->left;
    }
    int arrayIndex = 0;
    while (!isEmpty(stack)) {
        struct BST *curr = (struct BST *)pop(stack);
        treeValues[arrayIndex] = curr->value;
        arrayIndex++;
        curr = curr->right;
        while (curr != NULL) {
            push(stack, curr);
            curr = curr->left;
        }
    }
}

void binarySearchInsert(struct BST *tree, int *values, int lo, int hi) {
    if (lo == hi) {
        InsertBSTNode(tree, values[lo]);
        return;
    }
    int med = lo + (hi - lo) / 2;
    InsertBSTNode(tree, values[med]);
    binarySearchInsert(tree, values, lo, med - 1);
    binarySearchInsert(tree, values, med + 1, hi);
}

int BalanceBST(struct BST *tree) {
    int size = tree->size;
    int treeValues[size];
    InorderTraverse(tree, treeValues);
    free(tree);
    tree = CreateBST(); 
    binarySearchInsert(tree, treeValues, 0, size);
}

int BSTinterface(int argc, char *argv[]) {
    struct BST *tree = CreateBST();
    char command[255];
    int value;
    printf("Input command: ");
    scanf("%s", &command);
    if (strcmp(command, "help\0") == 0) {
        printf("help : list valid commands\n");
        printf("insert [value] : list valid commands\n");
        printf("remove [value] : remove node with given value from BST\n");
        printf("print inorder : print BST values via inorder traversal\n");
        printf("remove preorder : print BST values via preorder traversal\n");
        printf("remove postorder : print BST values via postorder traversal\n");
        printf("search [value] : check if tree contains value\n");
        printf("balance : balance BST\n");
    } else if (strcmp(command, "insert\0") == 0) {
        scanf("%d", value);
        InsertBSTNode(tree, value);
    } else if (strcmp(command, "remove\0") == 0) {
        scanf("%d", value);
        if (SearchTree(tree, value)) {
            RemoveBSTNode(tree, value);
            tree->size--;
        } else {
            printf("Error: tree does not contain value %d\n", value);
        }
    } else if (strcmp(command, "print inorder\0") == 0) {
        InorderPrint(tree);
    } else if (strcmp(command, "print preorder\0") == 0) {
        PreorderPrint(tree);
    } else if (strcmp(command, "print postorder\0") == 0) {
        PostorderPrint(tree);
    } else if (strcmp(command, "print postorder\0") == 0) {
        scanf("%d", &value);
        printf("%s", SearchTree(tree, value) ? "tree contains value\n" : "tree does not contain value\n");
    } else if (strcmp(command, "balance\0") == 0) {
        bool balanced = false;
        isBalanced(tree, &balanced);
        if (balanced) {
            printf("Tree is already balanced\n");
        } else {
            BalanceBST(tree);
        }
    }
}