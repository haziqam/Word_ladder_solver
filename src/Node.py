from collections import deque

class Node:
    def __init__(self, word, predecessor):
        self.word = word
        self.predecessor = predecessor

    def get_path_from_root(self):
        current = self
        path = []
        while current is not None:
            path.append(current.word)
            current = current.predecessor
        path.reverse()
        return path

class ExtendedNode(Node):
    def __init__(self, word, predecessor, distance_from_root):
        super().__init__(word, predecessor)
        self.distance_from_root = distance_from_root
