from collections import deque
from Node import Node, ExtendedNode
from PriorityQueue import PriorityQueue
# import enchant


# english_dict = enchant.Dict("en_US")
english_dict = set()
with open("src/dictionary.txt", "r") as f:
    for word in f:
        english_dict.add(word.strip())


def input_valid(starting_word: str, goal_word: str) -> bool:
    if not starting_word.isalpha(): return False 
    if not goal_word.isalpha(): return False 
    if len(starting_word) != len(goal_word): return False
    if starting_word not in english_dict: return False
    if goal_word not in english_dict: return False
    return True


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


def get_minimum_steps(current_word: str, goal_word: str):
    steps = 0
    for i in range(len(current_word)):
        if current_word[i] != goal_word[i]:
            steps += 1
    return steps


def BFS_solver(starting_word: str, goal_word: str):
    expand_node = Node(starting_word, None)
    queue = deque()
    visited = set()
    iterations = 0
    nodes_generated = 1

    queue.appendleft(expand_node)

    while queue:
        iterations += 1
        expand_node = queue.pop()

        if expand_node.word == goal_word:
            return (expand_node.get_path_from_root(), iterations, nodes_generated)

        possible_moves = get_possible_moves(expand_node.word)
        for word in possible_moves:
            if word not in visited:
                queue.appendleft(Node(word, expand_node))
                visited.add(word)
                nodes_generated += 1

    return (None, iterations, nodes_generated)


def DFS_solver(starting_word: str, goal_word: str):
    expand_node = Node(starting_word, None)
    stack = deque()
    visited = set()
    iterations = 0
    nodes_generated = 1

    stack.append(expand_node)
    visited.add(expand_node.word)

    while stack:
        iterations += 1
        expand_node = stack.pop()

        if expand_node.word == goal_word:
            return (expand_node.get_path_from_root(), iterations, nodes_generated)

        possible_moves = get_possible_moves(expand_node.word)
        for word in possible_moves:
            if word not in visited:
                stack.append(Node(word, expand_node))
                visited.add(word)
                nodes_generated += 1

    return (None, iterations, nodes_generated)


def greedy_solver(starting_word: str, goal_word: str):
    expand_node = Node(starting_word, None)
    queue = PriorityQueue()
    visited = set()
    iterations = 0
    nodes_generated = 1

    priority = get_minimum_steps(starting_word, goal_word)
    queue.enqueue(expand_node, priority)
    visited.add(expand_node.word)

    while not queue.is_empty():
        iterations += 1
        expand_node = queue.dequeue()

        if expand_node.word == goal_word:
            return (expand_node.get_path_from_root(), iterations, nodes_generated)

        possible_moves = get_possible_moves(expand_node.word)
        for word in possible_moves:
            if word not in visited:
                priority = get_minimum_steps(word, goal_word)
                queue.enqueue(Node(word, expand_node), priority)
                visited.add(word)
                nodes_generated += 1

    return (None, iterations, nodes_generated)


def UCS_solver(starting_word: str, goal_word: str):
    expand_node = ExtendedNode(starting_word, None, 0)
    queue = PriorityQueue()
    visited = set()
    iterations = 0
    nodes_generated = 1

    priority = expand_node.distance_from_root
    queue.enqueue(expand_node, priority)
    visited.add(expand_node.word)

    while not queue.is_empty():
        iterations += 1
        expand_node = queue.dequeue()

        if expand_node.word == goal_word :
            return (expand_node.get_path_from_root(), iterations, nodes_generated)

        possible_moves = get_possible_moves(expand_node.word)
        for word in possible_moves:
            if word not in visited:
                priority = dist_from_root = expand_node.distance_from_root + 1
                queue.enqueue(ExtendedNode(word, expand_node, dist_from_root), priority)
                visited.add(word)
                nodes_generated += 1

    return (None, iterations, nodes_generated)


def Astar_solver(starting_word: str, goal_word: str):
    expand_node = ExtendedNode(starting_word, None, 0)
    queue = PriorityQueue()
    visited = set()
    iterations = 0
    nodes_generated = 1

    priority = expand_node.distance_from_root + get_minimum_steps(starting_word, goal_word)
    queue.enqueue(expand_node, priority)
    visited.add(expand_node.word)

    while not queue.is_empty():
        iterations += 1
        expand_node = queue.dequeue()

        if expand_node.word == goal_word :
            return (expand_node.get_path_from_root(), iterations, nodes_generated)

        possible_moves = get_possible_moves(expand_node.word)
        for word in possible_moves:
            if word not in visited:
                dist_from_root = expand_node.distance_from_root + 1
                priority = dist_from_root + get_minimum_steps(word, goal_word)
                queue.enqueue(ExtendedNode(word, expand_node, dist_from_root), priority)
                visited.add(word)
                nodes_generated += 1

    return (None, iterations, nodes_generated)

if __name__ == "__main__":
    print(Astar_solver("vivid", "dowry"))