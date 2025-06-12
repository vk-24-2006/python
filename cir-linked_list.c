#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
    struct Node* next;
};

struct Node* head = NULL;
void insertAtEnd(int value)
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;

    if (head == NULL)
	{
        head = newNode;
        newNode->next = head;
    }
	 else
	{
        struct Node* temp = head;
        while (temp->next != head)
		{
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head;
    }
    printf("%d inserted into circular linked list\n", value);
}
void deleteFromBeginning()
{
    if (head == NULL)
	{
        printf("List is empty, cannot delete.\n");
        return;
    }

    struct Node* temp = head;
    if (head->next == head)
	{
        printf("Deleted element is %d\n", head->data);
        free(head);
        head = NULL;
    }
	 else 
	{
        struct Node* last = head;
        while (last->next != head)
		{
            last = last->next;
        }
        last->next = head->next;
        head = head->next;
        printf("Deleted element is %d\n", temp->data);
        free(temp);
    }
}
void display()
{
    if (head == NULL)
	{
        printf("Circular Linked List is empty.\n");
        return;
    }
    struct Node* temp = head;
    printf("Circular Linked List elements are:\n");
    do
	{
        printf("%d ", temp->data);
        temp = temp->next;
    }
	 while (temp != head);
    printf("\n");
}

int main()
{
    int choice, value;
    while (1)
	{
        printf("\n--- Circular Linked List Menu ---\n");
        printf("1. Insert\n2. Delete\n3. Display\n4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
		{
        case 1:
            printf("Enter value to insert: ");
            scanf("%d", &value);
            insertAtEnd(value);
            break;
        case 2:
            deleteFromBeginning();
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);
        default:
            printf("Invalid choice, try again.\n");
        }
    }
    return 0;
}
