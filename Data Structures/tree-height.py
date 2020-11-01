import sys

class node:
    """This is a node class for the nodes in the linked list we will be creating for the queue"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class linked_list:
    """This is the linked list data structure for the queue"""
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_node(self, data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = node(data)
            self.tail.next_node = new_node
            self.tail = new_node

    def pop_node(self):
        req_data = self.head.data
        self.head = self.head.next_node
        return req_data

class tree_height:
    """This class is to form the tree and calculate its height based on the given inputs"""
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parents = list(map(int, sys.stdin.readline().split()))

    def height(self):
        self.children = {}

        for i in range(self.n):
            self.children[i] = []

        for child in range(self.n):
            parent = self.parents[child]
            if parent != -1:
                self.children[parent].append(child)

        queue = linked_list()

        try:
            queue.insert_node(self.parents.index(-1))
        except ValueError:
            return 0

        height = 0
        queue_len = 1
        while True:
            if queue_len == 0:
                return height
            height += 1
            length = queue_len + 1
            while length > 1:
                i = queue.pop_node()
                length -= 1
                queue_len -= 1
                for k in self.children[i]:
                    queue.insert_node(k)
                    queue_len += 1



if __name__ == '__main__':
    tree = tree_height()
    tree.read()
    print(tree.height())