class LRUCache:

    def __init__(self, capacity: int):
        self._cap = capacity
        self._lru = dict()  # maps key -> node

        self._head = Node(None, None)
        self._tail = Node(None, None)

        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if self._lru.get(key) is None:
            return -1

        self._lru[key].prev.next = self._lru[key].next
        self._lru[key].next.prev = self._lru[key].prev

        self._lru[key].next = self._tail
        self._lru[key].prev = self._tail.prev

        self._tail.prev.next = self._lru[key]
        self._tail.prev = self._lru[key]

        return self._lru[key].val
        
    def put(self, key: int, value: int) -> None:

        if self._lru.get(key) is not None:
            node = self._lru[key]
            node.val = value

            node.prev.next = node.next
            node.next.prev = node.prev

            node.prev = self._tail.prev
            node.next = self._tail
            self._tail.prev.next = node
            self._tail.prev = node

            return

        if len(self._lru) == self._cap:
            deleteNode = self._head.next

            self._head.next = deleteNode.next
            deleteNode.next.prev = self._head

            del self._lru[deleteNode.key]
        
        newNode = Node(key, value)

        newNode.prev = self._tail.prev
        newNode.next = self._tail
        self._tail.prev.next = newNode
        self._tail.prev = newNode

        self._lru[key] = newNode


class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None