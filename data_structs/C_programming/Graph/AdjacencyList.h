struct AdjacencyList {
    int size;
    struct AdjacencyListNode *head;
    struct AdjacencyListNode *tail;
} typedef AdjacencyList;

struct AdjacencyListNode {
    int value;
    struct AdjacencyListNode *next;
} typedef AdjacencyListNode;

AdjacencyListNode *CreateAdjacencyListNode(int value);

AdjacencyList *createAdjacencyList();

void AddAdjacencyListNode(struct AdjacencyList *list, int value, int nodeIndex);

void RemoveAdjacencyListNode(struct AdjacencyList *list, int nodeIndex);

void ReverseAdjacencyList(struct AdjacencyList *list);

void PrintAdjacencyList(struct AdjacencyList *list, int nodeIndex);