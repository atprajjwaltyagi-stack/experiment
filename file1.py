class SLLNode:
    """A node for a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = SLLNode(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = SLLNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_head(data)
            return
        new_node = SLLNode(data)
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if not current:
            print("Error: Index out of bounds.")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_by_key(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print(f"Delete failed: Key '{key}' not found.")
            return
        prev.next = current.next

    def traverse(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("SLL (Forward):", " -> ".join(elements))

print("--- Testing Singly Linked List ---")
sll = SinglyLinkedList()
sll.insert_at_tail(10)
sll.insert_at_head(5)
sll.insert_at_index(2, 15)
sll.traverse() 
sll.delete_by_key(10)
sll.traverse()