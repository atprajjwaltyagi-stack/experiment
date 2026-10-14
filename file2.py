class DLLNode:
    """A node for a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        """Inserts a new node at the tail of the list."""
        new_node = DLLNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete(self, key):
        """Deletes the first node matching the target data key."""
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else: 
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
        print(f"Delete failed: Key '{key}' not found.")

    def reverse_traverse(self):
        """Traverses and prints the list from tail back to head."""
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("DLL (Reverse):", " <-> ".join(elements))
print("\n--- Testing Doubly Linked List ---")
dll = DoublyLinkedList()
dll.insert(50)
dll.insert(60)
dll.insert(70)
dll.delete(60)
dll.reverse_traverse()