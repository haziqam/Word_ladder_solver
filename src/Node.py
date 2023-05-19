from collections import deque

class Node:
    def __init__(self, word, predecessor):
        self.word = word
        self.predecessor = predecessor

    def get_path_from_root(self):
        current = self
        path = deque()
        while (current != None):
            path.appendleft(current.word)
            current = current.predecessor
        return list(path)


if __name__ == "__main__":
    a = Node("heal", None)

    b = Node("heap", a)

    c = Node("hear", a)

    d = Node("pear", c)

    e = Node("bear", d)

    f = Node("tear", e)

    print(b.get_path_from_root())

    print(f.get_path_from_root())