class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def display(self):
        current = self
        while current is not None:
            print(current.data)
            current = current.next


head = Node()
current = head

for i in range(5):
    # Create a new node and link it to the current node
    current.next = Node()
    current = current.next
    current.data = input(f"Enter the data {i}:\n")

# Display the linked list
head.display()
