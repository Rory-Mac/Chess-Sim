#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "AdjacencyList.h"
#include "Stack.h"

struct Graph {
    int size;
    AdjacencyList **adjacencyLists;
} typedef Graph;

Graph *createGraph(int graphSize) {
    Graph *newGraph = (Graph *)malloc(sizeof(Graph));
    newGraph->size = graphSize;
    newGraph->adjacencyLists = (AdjacencyList **)malloc(graphSize * sizeof(AdjacencyList *));
    for (int i = 0; i < graphSize; i++) {
        newGraph->adjacencyLists[i] = createAdjacencyList();
    }
    return newGraph;
}

void addEdge(Graph *graph, int v, int w) {
    AddAdjacencyListNode(graph->adjacencyLists[v], w, 1);
}

void removeEdge(Graph *graph, int v, int w) {
    RemoveAdjacencyListNode(graph->adjacencyLists[v], w);
}

void bfs(Graph *graph, int v) {
    bool visited[graph->size];
    Stack *stack = createStack(graph->size);
    push(stack, v);
    printf("%d ", v);
    while (!isEmpty(stack)) {
        int currVertice = pop(stack);
        visited[currVertice] = true;
        AdjacencyList *list = graph->adjacencyLists[currVertice];
        AdjacencyListNode *node = list->head;
        while (node != NULL) {
            if (!visited[node->value]) {
                printf("%d ", node->value);
                push(stack, node->value);
            }
            node = node->next;
        }
    }
    printf("\n");
}

void dfs(Graph *graph, int v) {
    bool visited[graph->size];
    Stack *stack = createStack(graph->size);
    push(stack, v);
    while (!isEmpty(stack)) {
        int currVertice = pop(stack);
        printf("%d ", currVertice);
        visited[currVertice] = true;
        AdjacencyList *list = graph->adjacencyLists[currVertice];
        AdjacencyListNode *node = list->head;
        while (node != NULL) {
            if (!visited[node->value]) {
                push(stack, node->value);
            }
            node = node->next;
        }
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    Graph *graph = createGraph(9);
    char command[255];
    int v, w;
    while (true) {
        printf("Input Instruction: ");
        scanf("%s", &command);
        if (strcmp(command, "help\0") == 0) {
            printf("\tadd [v] [w] : add edge from vertex v to vertex w\n");
            printf("\tremove [v] [w] : remove edge from vertex v to vertex w\n");
            printf("\tbfs [v]: print bfs traversal of graph from initial vertex v\n");
            printf("\tdfs [v]: print dfs traversal of graph from initial vertex v\n");
        } else if (strcmp(command, "add\0") == 0) {
            scanf("%d %d", &v, &w);
            addEdge(graph, v, w);
        } else if (strcmp(command, "remove\0") == 0) {
            scanf("%d %d", &v, &w);
            removeEdge(graph, v, w);
        } else if (strcmp(command, "bfs\0") == 0) {
            scanf("%d", &v);
            bfs(graph, v);
        } else if (strcmp(command, "dfs\0") == 0) {
            scanf("%d", &v);
            dfs(graph, v);
        } else if (strcmp(command, "exit\0") == 0) {
            break;
        } else {
            printf("Input unknown, type 'help' for list of commands.\n");
        }
    }
    return 0;
}
