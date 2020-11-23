# python3

import sys


class Node:
    def __init__(self):
        self.data = None
        self.next_node = None
        self.previous_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node()
        new_node.data = data
        if self.head:
            self.head.previous_node = new_node
        new_node.next_node = self.head
        self.head = new_node

    def delete_node(self, data):
        if self.head:
            current_node = self.head
            while current_node.next_node:
                if current_node == self.head:
                    if current_node.data == data:
                        current_node.next_node.previous_node = None
                        self.head = current_node.next_node

                else:
                    if current_node.data == data:
                        current_node.next_node.previous_node = current_node.previous_node
                        current_node.previous_node.next_node = current_node.next_node

                current_node = current_node.next_node

            if current_node.data == data and current_node == self.head:
                self.head = None

            elif current_node.data == data:
                current_node.previous_node.next_node = None

    def find_node(self, data):
        if self.head:
            current_node = self.head
            while current_node.next_node:
                if current_node.data == data:
                    return "yes"

                current_node = current_node.next_node
            if current_node.data == data:
                return "yes"
        return "no"

    def check(self):
        if self.head:
            current_node = self.head
            while current_node.next_node:
                print(current_node.data, end=" ")
                current_node = current_node.next_node
            print(current_node.data)
        else:
            print()


class HashMap:
    """ This is a class for the HashMap data structure built on an arrays """

    def __init__(self):
        self.n = None
        self.query = None
        self.argument = None
        self.PhoneBook = None
        self.p = 1000000007
        self.m = None
        self.x = 263
        self.hashkey = None

    def read(self):
        self.m = int(sys.stdin.readline())
        self.n = int(sys.stdin.readline())
        self.PhoneBook = []
        for _ in range(self.m):
            self.PhoneBook.append(LinkedList())
        for _ in range(self.n):
            self.query, self.argument = sys.stdin.readline().rstrip('\n').split(' ')
            self.hashkey = 0
            for i in range(len(self.argument)):
                self.hashkey += (ord(self.argument[i]) * (self.x**i))%self.p

            self.hashkey = self.hashkey % self.m

            if self.query == "add":
                if self.PhoneBook[self.hashkey].find_node(self.argument) == "no":
                    self.PhoneBook[self.hashkey].insert_node(self.argument)
            elif self.query == "del":
                self.PhoneBook[self.hashkey].delete_node(self.argument)
            elif self.query == "find":
                print(self.PhoneBook[self.hashkey].find_node(self.argument))
            elif self.query == "check":
                self.PhoneBook[int(self.argument)].check()

if __name__ == "__main__":
    test_list = HashMap()
    test_list.read()