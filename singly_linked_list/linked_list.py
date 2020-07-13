class Node:
    """
    Data:
    Stores two pieces of data:
    1. The Value
    2. The Next Node

    Methods/Behavior/Operations:
    1. Get Value
    2. Set Value
    3. Get Next
    4. Set Next
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList:
    """
    Data:
    1. A reference to the head node.
    2. A reference to the tail node.

    Behavior/methods:
    1. Append (Add a new node to the Node referenced by the Tail)
    2. Prepend (Add a new node and point that Node;s next_node at the old Head; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, node):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # Empty LL
        if self.head is None:
            return None
        # LL of one item
        if self.head.get_next() is None:
            head = self.head

            self.head = None

            self.tail = None

            return head.get_value()

        # More than one item
        value = self.head.get_value
        self.head = self.head.get_next()
        return value

