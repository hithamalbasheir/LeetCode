class Node:
    def __init__(self):
        self.keys = set()
        self.count = 0
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_count = {}      # Key -> Count
        self.count_node = {}     # Count -> Node

        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, prev_node, new_node):
        """Adds new_node after prev_node."""
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        """Removes node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            node = self.count_node[count]
            node.keys.remove(key)
            # Add to the next count node
            if count + 1 in self.count_node:
                next_node = self.count_node[count + 1]
            else:
                next_node = Node()
                next_node.count = count + 1
                self.count_node[count + 1] = next_node
                self._add_node_after(node, next_node)
            next_node.keys.add(key)
            self.key_count[key] = count + 1
            # Remove the old node if it's empty
            if not node.keys:
                self._remove_node(node)
        else:
            # Key is new, add to count 1 node
            if 1 in self.count_node:
                node = self.count_node[1]
            else:
                node = Node()
                node.count = 1
                self.count_node[1] = node
                self._add_node_after(self.head, node)
            node.keys.add(key)
            self.key_count[key] = 1

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        count = self.key_count[key]
        node = self.count_node[count]
        node.keys.remove(key)
        if count == 1:
            # Remove the key entirely
            del self.key_count[key]
        else:
            # Add to the previous count node
            if count - 1 in self.count_node:
                prev_node = self.count_node[count - 1]
            else:
                prev_node = Node()
                prev_node.count = count - 1
                self.count_node[count - 1] = prev_node
                self._add_node_after(node.prev, prev_node)
            prev_node.keys.add(key)
            self.key_count[key] = count - 1
        # Remove the old node if it's empty
        if not node.keys:
            self._remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        node = self.tail.prev
        return next(iter(node.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        node = self.head.next
        return next(iter(node.keys))