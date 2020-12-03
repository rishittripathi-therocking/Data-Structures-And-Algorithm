# python3

import sys, threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)

class TreeNode:
    def __init__(self):
        self.key = None
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.visited = False

class QueueNode:
    def __init__(self):
        self.key = None
        self.next_node = None
        self.previous_node = None

class Tree:
    def __init__(self):
        self.root = None
        self.n = 0
        self.vertex = 0

    def insert(self, parent, vertex, index, data):
        vertex.key = int(data[index][0])
        vertex.parent = parent
        if int(data[index][1]) != -1:
            left_node = TreeNode()
            vertex.left_child = left_node
            self.insert(vertex, left_node, int(data[index][1]), data)
        if int(data[index][2]) != -1:
            right_node = TreeNode()
            vertex.right_child = right_node
            self.insert(vertex, right_node, int(data[index][2]), data)


    def in_order(self):
        i = self.n
        vertex = self.root
        new_queue = Queue()
        while i > 0:
            if vertex.visited:
                if vertex.right_child:
                    if vertex.right_child.visited:
                        vertex = vertex.parent
                    else:
                        vertex = vertex.right_child
                else:
                    vertex = vertex.parent
            else:
                if vertex.left_child:
                    if vertex.left_child.visited:
                        new_queue.insert(vertex.key)
                        i -= 1
                        vertex.visited = True
                    else:
                        vertex = vertex.left_child
                else:
                    new_queue.insert(vertex.key)
                    i -= 1
                    vertex.visited = True
        new_queue.print()

    def pre_order(self):
        i = self.n
        vertex = self.root
        prequeue = Queue()
        while i > 0:
            if vertex.visited:
                prequeue.insert(vertex.key)
                # print(vertex.key)
                vertex.visited = False
                i -= 1
                if vertex.left_child:
                    if vertex.left_child.visited:
                        vertex = vertex.left_child
                    elif vertex.right_child:
                        if vertex.right_child.visited:
                            vertex = vertex.right_child
                        else:
                            vertex = vertex.parent
                    else:
                        vertex = vertex.parent
                elif vertex.right_child:
                    if vertex.right_child.visited:
                        vertex = vertex.right_child
                    else:
                        vertex = vertex.parent
                else:
                    vertex = vertex.parent

            else:
                if vertex.right_child:
                    if vertex.right_child.visited:
                        vertex = vertex.right_child
                    else:
                        vertex = vertex.parent
                else:
                    vertex = vertex.parent

        prequeue.print()

    def post_order(self):
        vertex = self.root
        i = self.n
        postqueue = Queue()
        while i > 0:
            if not vertex.visited:
                if vertex.left_child:
                    if not vertex.left_child.visited:
                        vertex = vertex.left_child
                    elif vertex.right_child:
                        if not vertex.right_child.visited:
                            vertex = vertex.right_child
                        else:
                            postqueue.insert(vertex.key)
                            i -= 1
                            vertex.visited = True
                            vertex = vertex.parent
                    else:
                        postqueue.insert(vertex.key)
                        i -= 1
                        vertex.visited = True
                        vertex = vertex.parent
                elif vertex.right_child:
                    if not vertex.right_child.visited:
                        vertex = vertex.right_child
                    else:
                        postqueue.insert(vertex.key)
                        i -= 1
                        vertex.visited = True
                        vertex = vertex.parent
                else:
                    postqueue.insert(vertex.key)
                    i -= 1
                    vertex.visited = True
                    vertex = vertex.parent
        postqueue.print()

    def printTree(self, vertex):
        print(vertex.key)
        if vertex.left_child:
            print(vertex.key)
            print('left')
            self.printTree(vertex.left_child)
        if vertex.right_child:
            print(vertex.key)
            print('right')
            self.printTree(vertex.right_child)

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key):
        if not self.head:
            new_node = QueueNode()
            self.head = new_node
            self.head.key = key
            self.tail = self.head
            self.previous_node = self.head

        else:
            new_node = QueueNode()
            self.tail.next_node = new_node
            new_node.previous_node = self.tail
            self.tail = new_node
            new_node.key = key

    def print(self):
        vertex = self.head
        while vertex != self.tail:
            print(vertex.key, end = ' ')
            vertex = vertex.next_node
        print(vertex.key)

def main():
    new_tree = Tree()
    new_tree.n = int(sys.stdin.readline())
    new_tree.root = TreeNode()
    data = []
    # f = open('tests/21', 'r')
    # new_tree.n = int(f.readline())
    # for i in range(new_tree.n):
    #     data.append(f.readline().rstrip('\n').split(' '))
    for i in range(new_tree.n):
        data.append(sys.stdin.readline().rstrip('\n').split(' '))
    new_tree.insert(new_tree.root, new_tree.root, 0, data)
    # new_tree.printTree(new_tree.root)
    new_tree.in_order()
    new_tree.pre_order()
    new_tree.post_order()

threading.Thread(target=main).start()