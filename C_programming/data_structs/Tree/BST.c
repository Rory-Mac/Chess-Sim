#include <stdio.h>
#include <stdbool.h>
#include "Stack.h"

struct BST {
    int value;
    int size;
    struct BST *left;
    struct BST *right;
};

struct BST *CreateBST() {
    struct BST *newTree = malloc(sizeof(struct BST));
    newTree->value = 0;
    newTree->left = NULL;
    newTree->right = NULL;
}

int InsertBSTNode(struct BST *tree, int value) {
    struct BST *curr = tree;
    if (tree->value > value) {
        if (tree->left == NULL) {
            struct BST *newTree = createBST();
            newTree->value = value;
            tree->left = newTree;
            return 0;
        }
        return InsertBSTNode(tree->left, value);
    } else if (tree->value < value) {
        if (tree->right == NULL) {
            struct BST *newTree = createBST();
            newTree->value = value;
            tree->right = newTree;
            return 0;
        }
        return InsertBSTNode(tree->right, value);
    }
    printf("Error: value already exists in BST\n");
    return -1;
}

void RemoveBSTNode(struct BST *tree, int value) {
    if (tree == NULL) return;
    if (tree->left == value) {
        struct BST *left_subtree = tree->left->left;
        struct BST *right_subtree = tree->left->right;
        free(tree->left);
        tree->left = right_subtree;
        struct BST *curr = right_subtree;
        while (curr->left != NULL) {
            curr = curr->left;
        }
        curr->left = left_subtree;
    } else if (tree->right == value) {
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
    return max(depth_left, depth_right) + 1;
}

int BalanceBST(struct BST *tree) {
    int treeValues[tree->size];
    InorderSave(tree, treeValues);
}

int main(int argc, char *argv[]) {
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
        if (InsertBSTNode(tree, value) == 0) {
            tree->size ++;
        };
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


// balance, check memory leaks