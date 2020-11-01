#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max=999999999999

    def Push(self, a):
        if top == -1:
            self.max=a
            self.__stack.append(a)
        else:
            self.__stack.append(a)
            self.max<a:
                self.max=a
            


    def Pop(self):
        assert(len(self.__stack))

        if self.__stack.pop()==self.max:
            self.max=self.__stack.peek()

    def Max(self):
        assert(len(self.__stack))
        return self.max


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
