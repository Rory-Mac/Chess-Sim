#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#define MAP_SIZE 64
#define MAX_COLLISIONS 256

struct HashMap {
    char ***map;
} typedef HashMap;

HashMap *createHashMap() {
    HashMap *hashMap = malloc(sizeof(HashMap));
    hashMap->map = malloc(MAP_SIZE * sizeof(char **));
    for (int i = 0; i < MAP_SIZE; i++) {
        hashMap->map[i] = malloc(MAX_COLLISIONS * sizeof(char *));
        for (int j = 0; j < MAX_COLLISIONS; j++) {
            hashMap->map[i][j] = (char *)NULL;
        }
    }
    return hashMap;
}

// modified from Dan Bernstein's hash function, http://www.cse.yorku.ca/~oz/hash.html
int hash(char *word) {
    int hash = 5381;
    int c;
    while (c = *word++)
        hash = ((hash << 5) + hash) + c;
    return hash % MAP_SIZE;
}

void addHashItem(HashMap *hashMap, char *word) {
    int i = hash(word);
    int inserted = false;
    for (int j = 0; j < MAX_COLLISIONS; j++) {
        if (strcmp(hashMap->map[i][j], (char *)NULL)) {
            hashMap->map[i][j] = malloc(strlen(word) + 1);
            memcpy(hashMap->map[i][j], word, strlen(word) + 1);
            inserted = true;
            break;
        }
    }
    if (!inserted) {
        printf("Error: Add hash item failed: Maximum allowed hash collisions exceeded.\n");
    }
}

void removeHashItem(HashMap *hashMap, char *word) {
    int i = hash(word);
    int removed = false;
    for (int j = 0; j < MAX_COLLISIONS; j++) {
        if (strcmp(word, hashMap->map[i][j]) == 0) {
            free(hashMap->map[i][j]);
            hashMap->map[i][j] = (char *)NULL;
            removed = true;
            break;
        }
    }
    if (!removed) {
        printf("Error: remove hash item failed: item not found in hash map.\n");
        return;
    }
}

void containsHashItem(HashMap *hashMap, char *word) {
    int i = hash(word);
    for (int j = 0; j < MAX_COLLISIONS; j++) {
        if (strcmp(word, hashMap->map[i][j]) == 0) {
            printf("Hash map contains item.\n");
            return;
        }
    }
    printf("Hash map does not contain item.\n");
}

void freeHashMap(HashMap *hashMap) {
    for (int i = 0; i <= MAP_SIZE; i++) {
        for (int j = 0; j <+ MAX_COLLISIONS; j++) {
            free(hashMap->map[i][j]);
        }
        free(hashMap->map[i]);
    }
    free(hashMap->map);
    free(hashMap);
}

int main() {
    HashMap *hashMap = createHashMap();
    char command[255];
    char word[255];
    while (true) {
        printf("Input Instruction: ");
        scanf("%s", &command);
        if (strcmp(command, "help\0") == 0) {
            printf("\thelp : lists all valid commands\n");
            printf("\tadd [word] : add word to hash map\n");
            printf("\tremove [word] : remove word from hash map \n");
            printf("\tcontains [word] : check if hash map contains word\n");
            printf("\texit : exit command interface\n");
        } else if (strcmp(command, "add\0") == 0) {
            scanf("%s", &word);
            addHashItem(hashMap, word);
        } else if (strcmp(command, "remove\0") == 0) {
            scanf("%s", &word);
            removeHashItem(hashMap, word);
        } else if (strcmp(command, "contains\0") == 0) {
            scanf("%s", &word);
            containsHashItem(hashMap, word);
        } else if (strcmp(command, "exit\0") == 0) {
            break;
        } else {
            printf("Input unknown, type 'help' to list all commands.\n");
        }
    }
    return 0;
}