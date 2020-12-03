#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree, vertex, min_val, max_val):
    if min_val:
        if max_val:
            if tree[vertex][0] < max_val and tree[vertex][0] > min_val:
                if tree[vertex][1] != -1:
                    # print('left', tree[vertex][0], min_val, tree[vertex][0])
                    if not IsBinarySearchTree(tree, tree[vertex][1], min_val, tree[vertex][0]):
                        # print('left', tree[vertex][0], min_val, tree[vertex][0])
                        return False
                if tree[vertex][2] != -1:
                    # print('right', tree[vertex][0], tree[vertex][0], max_val)
                    if not IsBinarySearchTree(tree, tree[vertex][2], tree[vertex][0], max_val):
                        # print('right', tree[vertex][0], tree[vertex][0], max_val)
                        return False
                # if tree[vertex][1] == -1 and tree[vertex][2] == -1:
                #     return True
            else:
                return False
        else:
            if tree[vertex][0] > min_val:
                if tree[vertex][1] != -1:
                    # print('left', tree[vertex][0], min_val, tree[vertex][0])
                    if not IsBinarySearchTree(tree, tree[vertex][1], min_val, tree[vertex][0]):
                        # print('left', tree[vertex][0], min_val, tree[vertex][0])
                        return False
                if tree[vertex][2] != -1:
                    # print('right', tree[vertex][0], tree[vertex][0], max_val)
                    if not IsBinarySearchTree(tree, tree[vertex][2], tree[vertex][0], max_val):
                        # print('right', tree[vertex][0], tree[vertex][0], max_val)
                        return False
                # if tree[vertex][1] == -1 and tree[vertex][2] == -1:
                #     return True
            else:
                return False
    elif max_val:
        if tree[vertex][0] < max_val:
            if tree[vertex][1] != -1:
                # print('left', tree[vertex][0], min_val, tree[vertex][0])
                if not IsBinarySearchTree(tree, tree[vertex][1], min_val, tree[vertex][0]):
                    # print('left', tree[vertex][0], min_val, tree[vertex][0])
                    return False
            if tree[vertex][2] != -1:
                # print('right', tree[vertex][0], tree[vertex][0], max_val)
                if not IsBinarySearchTree(tree, tree[vertex][2], tree[vertex][0], max_val):
                    # print('right', tree[vertex][0], tree[vertex][0], max_val)
                    return False
            # if tree[vertex][1] == -1 and tree[vertex][2] == -1:
            #     return True
        else:
            return False
    else:
        if tree[vertex][1] != -1:
            # print('left', tree[vertex][0], min_val, tree[vertex][0])
            if not IsBinarySearchTree(tree, tree[vertex][1], min_val, tree[vertex][0]):
                # print('left', tree[vertex][0], min_val, tree[vertex][0])
                return False
        if tree[vertex][2] != -1:
            if not IsBinarySearchTree(tree, tree[vertex][2], tree[vertex][0], max_val):
                # print('right', tree[vertex][0], tree[vertex][0], max_val)
                return False
        # if tree[vertex][1] == -1 and tree[vertex][2] == -1:
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if nodes == 0 or IsBinarySearchTree(tree, 0, None, None):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()