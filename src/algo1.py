import timeit
from collections import deque
from Node import Node
# import enchant

# english_dict = enchant.Dict("en_US")
english_dict = set()
with open("dictionary.txt", "r") as f:
    for word in f:
        english_dict.add(word.strip())

def get_possible_moves(current_word: str):
    possible_moves = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(current_word)):
        for letter in alphabet:
            if letter == current_word[i]:
                continue

            constructed_word = current_word[:i] + letter + current_word[i + 1:]
            if constructed_word in english_dict:
                possible_moves.append(constructed_word)

    return possible_moves

def BFS_solver(starting_word: str, goal_word: str):
    expandNode = Node(starting_word, None)
    queue = deque()
    visited = set()

    queue.appendleft(expandNode)
    visited.add(expandNode.word)

    while queue:
        expandNode = queue.pop()

        if expandNode.word == goal_word:
            print(expandNode.get_path_from_root())
            return

        possible_moves = get_possible_moves(expandNode.word)
        for word in possible_moves:
            if word not in visited:
                queue.appendleft(Node(word, expandNode))
                visited.add(word)

    print("No path found.")

def DFS_solver(starting_word: str, goal_word: str):
    expandNode = Node(starting_word, None)
    stack = deque()
    visited = set()

    stack.append(expandNode)
    visited.add(expandNode.word)

    while stack:
        expandNode = stack.pop()

        if expandNode.word == goal_word:
            print(expandNode.get_path_from_root())
            return

        possible_moves = get_possible_moves(expandNode.word)
        for word in possible_moves:
            if word not in visited:
                stack.append(Node(word, expandNode))
                visited.add(word)

    print("No path found.")

if __name__ == "__main__":
    BFS_solver("give", "take")
    DFS_solver("give", "take")
