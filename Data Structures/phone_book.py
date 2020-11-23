import sys


class HashMap:
    """ This is a class for the HashMap data structure built on an arrays """
    def __init__(self):
        self.n = None
        self.query = None
        self.arguments = None
        self.PhoneBook = None
        self.a = 34
        self.b = 24
        self.p = 100019
        self.m = 1000
        self.hashkey = None

    def read(self):
        self.n = int(sys.stdin.readline())
        self.PhoneBook = [{} for _ in range(self.m)]
        for _ in range(self.n):
            self.query, *self.arguments = sys.stdin.readline().rstrip('\n').split(' ')
            self.hashkey = (((self.a * int(self.arguments[0]))+self.b) % self.p) % self.m
            if self.query == "add":
                self.add()
            elif self.query == "del":
                self.delete()
            elif self.query == "find":
                self.find()

    def add(self):
        self.PhoneBook[self.hashkey][int(self.arguments[0])] = self.arguments[1]

    def delete(self):
        if int(self.arguments[0]) in self.PhoneBook[self.hashkey]:
            del self.PhoneBook[self.hashkey][int(self.arguments[0])]

    def find(self):
        if int(self.arguments[0]) in self.PhoneBook[self.hashkey]:
            print(self.PhoneBook[self.hashkey][int(self.arguments[0])])
        else:
            print('not found')


if __name__ == "__main__":
    phone_book = HashMap()
    phone_book.read()