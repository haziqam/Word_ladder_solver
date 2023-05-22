import time
from Algorithms import input_valid, BFS_solver, DFS_solver, UCS_solver, greedy_solver, Astar_solver

def main():
    starting_word = input("Insert starting word: ").strip().lower()
    goal_word = input("Insert goal word: ").strip().lower()
    print("\n\n")

    if not input_valid(starting_word, goal_word):
        print("Masukan tidak valid")
        return

    for solver in (BFS_solver, DFS_solver, UCS_solver, greedy_solver, Astar_solver):
        start_time = time.perf_counter()
        result = solver(starting_word, goal_word)
        finish_time = time.perf_counter()
        print(f"===== Algorithm: {solver.__name__} =====")
        print(f"Number of iterations: {result[1]}")
        print(f"Number of nodes generated: {result[2]}")
        print(f"Execution time: {finish_time - start_time} seconds")

        if result[0] is None:
            print("No solution found")
        else:
            print(f"Number of steps: {len(result[0]) - 1}")
            print(" -> ".join(result[0]))

        print("\n\n")

if __name__ == "__main__":
    main()