#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

struct BSTNode typedef BSTNode;

struct BSTNode {
    int value;
    BSTNode *left;
    BSTNode *right;
};

struct BST {
    int size;
    BSTNode *root;
} typedef BST;


BST *createBST() {
    BST *newBST = (BST *)malloc(sizeof(BST));
    newBST->size = 0;
    newBST->root = NULL;
}

void freeBSTtraversal(BSTNode *tree) {
    if (tree == NULL) return;
    freeBSTtraversal(tree->left);
    freeBSTtraversal(tree->right);
    free(tree);
}

void freeBST(BST *tree) {
    freeBSTtraversal(tree->root);
    free(tree);
}

BSTNode *createBSTNode(int value) {
    BSTNode *newNode = (BSTNode *)malloc(sizeof(BSTNode));
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void insertBST(BST *tree, int value) {
    BSTNode *newNode = createBSTNode(value);
    tree->size++;
    if (tree->root == NULL) {
        tree->root = newNode;
        return;
    }
    BSTNode *curr = tree->root;
    while (true) {
        if (value < curr->value ) {
            if (curr->left == NULL) {
                curr->left = newNode;
                break;
            } 
            curr = curr->left;
        } else if (value > curr->value) {
            if (curr->right == NULL) {
                curr->right = newNode;
                break;
            }
            curr = curr->right;
        } else if (value == curr->value) {
            printf("value already stored in tree\n");
            tree->size--;
            break;
        }
    }
}

void removeBST(BST *tree, int value) {
    BSTNode *curr = tree->root;
    if (tree->root == NULL) {
        printf("Value not found in binary search tree\n");
    } else if (tree->root->value == value) {
        BSTNode *left_subtree = curr->left;
        BSTNode *right_subtree = curr->right;
        free(curr);
        if (left_subtree == NULL) {
            tree->root = right_subtree;
            return;
        }
        if (right_subtree == NULL) {
            tree->root = left_subtree;
            return;
        }
        tree->root = right_subtree;
        curr = right_subtree;
        while (curr->left != NULL) {
            curr = curr->left;
        }
        curr->left = left_subtree;
        return;
    }
    while (curr != NULL) {
        if (value < curr->value) {
            if (curr->left != NULL && curr->left->value == value) {
                BSTNode *left_subtree = curr->left->left;
                BSTNode *right_subtree = curr->left->right;
                free(curr->left);
                if (right_subtree == NULL) {
                    curr->left = left_subtree;
                    return;
                }
                if (left_subtree == NULL) {
                    curr->left = right_subtree;
                    return;
                }
                curr->left = right_subtree;
                curr = right_subtree;
                while (curr->left != NULL) {
                    curr = curr->left;
                }
                curr->left = left_subtree;
                return;
            }
            curr = curr->left;
        } else if (value > curr->value) {
            if (curr->right != NULL && curr->right->value == value) {
                BSTNode *left_subtree = curr->right->left;
                BSTNode *right_subtree = curr->right->right;
                free(curr->right);
                if (left_subtree == NULL) {
                    curr->right = right_subtree;
                    return;
                }
                if (right_subtree == NULL) {
                    curr->right = left_subtree;
                    return;
                }
                curr->right = left_subtree;
                curr = left_subtree;
                while (curr->right != NULL) {
                    curr = curr->right;
                }
                curr->right = right_subtree;
                return;
            }
            curr = curr->right;
        }
    }
    printf("Value not found in binary search tree\n");
}

void invertBST(BSTNode *tree) {
    if (tree == NULL) return;
    invertBST(tree->left);
    invertBST(tree->right);
    BSTNode *temp = tree->left;
    tree->left = tree->right;
    tree->right = temp;
}

void printInorder(BSTNode *tree) {
    if (tree == NULL) return;
    printInorder(tree->left);
    printf("%d ", tree->value);
    printInorder(tree->right);
}

void printPreorder(BSTNode *tree) {
    if (tree == NULL) return;
    printf("%d ", tree->value);
    printInorder(tree->left);
    printInorder(tree->right);
}

void printPostorder(BSTNode *tree) {
    if (tree == NULL) return;
    printInorder(tree->left);
    printInorder(tree->right);
    printf("%d ", tree->value);
}

int main(int argc, char *argv[]) {
    BST *tree = createBST();
    char command[255];
    int value;
    while (true) {
        printf("Input Instruction: ");
        scanf("%s", &command);
        if (!strcmp(command, "help\0")) {
            printf("\tinsert [value] : insert [value] into binary search tree\n");
            printf("\tremove [value] : remove [value] from binary search tree\n");
            printf("\tinvert : invert binary search tree\n");
            printf("\tinorder : print tree elements using inorder traversal\n");
            printf("\tpreorder : print tree elements using preorder traversal\n");
            printf("\tpostorder : print tree elements using postorder traversal\n");
            printf("\thelp : list valid commands\n");
            printf("\texit : exit command interface\n");
        } else if (!strcmp(command, "insert\0")) {
            scanf("%d", &value);
            insertBST(tree, value);
        } else if (!strcmp(command, "remove\0")) {
            scanf("%d", &value);
            removeBST(tree, value);
        } else if (!strcmp(command, "invert\0")) {
            invertBST(tree->root);
        } else if (!strcmp(command, "inorder\0")) {
            printInorder(tree->root);
            printf("\n");
        } else if (!strcmp(command, "preorder\0")) {
            printPreorder(tree->root);
            printf("\n");
        } else if (!strcmp(command, "postorder\0")) {
            printPostorder(tree->root);
            printf("\n");
        } else if (!strcmp(command, "exit\0")) {
            break;
        } else {
            printf("Input unknown, type 'help' for list of commands.\n");
        }
    }
    freeBST(tree);
    return 0;
}