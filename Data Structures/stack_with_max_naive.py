import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_stack = []

    def Push(self, a):
        if len(self.max_stack) > 0:
            if a > self.max_stack[-1]:
                self.max_stack.append(a)
            else:
                self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(a)
        self.__stack.append(a)

    def Pop(self):
        self.max_stack.pop()
        self.__stack.pop()

    def Max(self):
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)