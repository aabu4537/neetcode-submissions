class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_map = {}

        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node = self.node_map[key]
        self.remove(node)
        self.add(node)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            old_node = self.node_map[key]
            self.remove(old_node)
            del self.node_map[key]
        
        node = ListNode(key, value)
        self.add(node)
        self.node_map[key] = node

        if len(self.node_map) >  self.capacity:
            delete = self.head.next
            self.remove(delete)
            del self.node_map[delete.key]


    
    def add(self, node):
        prev_end = self.tail.prev

        node.prev = prev_end
        node.next = self.tail
        
        prev_end.next = node
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        
