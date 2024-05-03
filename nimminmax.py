class NimGame:
    def _init_(self, heaps):
        self.heaps = heaps

    def display_heaps(self):
        for i, heap in enumerate(self.heaps):
            print(f"Heap {i + 1}: {'*' * heap}")

    def take_turn(self, limit):
        print("Current state of heaps:")
        self.display_heaps()
        while True:
            heap_index = int(input("Select a heap (1, 2, 3, ...): ")) - 1
            if 0 <= heap_index < len(self.heaps) and self.heaps[heap_index] > 0:
                break
            else:
                print("Invalid heap selection. Try again.")
        while True:
            matchsticks = int(input(f"How many matchsticks do you want to remove? (1-{limit}) "))
            if 1 <= matchsticks <= limit and matchsticks <= self.heaps[heap_index]:
                break
            else:
                print("Invalid number of matchsticks or exceeds the limit. Try again.")
        self.heaps[heap_index] -= matchsticks

    def game_over(self):
        return sum(self.heaps) == 0

def alphabeta(heaps, depth, alpha, beta, is_maximizing, limit):
    if depth == 0 or sum(heaps) == 0:
        return sum(heaps), None

    if is_maximizing:
        max_score = float('-inf')
        best_move = None
        for i, heap in enumerate(heaps):
            if heap > 0:
                for matchsticks_to_remove in range(1, min(heap, limit) + 1):
                    new_heaps = heaps[:]
                    new_heaps[i] -= matchsticks_to_remove
                    score, _ = alphabeta(new_heaps, depth - 1, alpha, beta, False, limit)
                    if score > max_score:
                        max_score = score
                        best_move = (i, matchsticks_to_remove)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return max_score, best_move
    else:
        min_score = float('inf')
        best_move = None
        for i, heap in enumerate(heaps):
            if heap > 0:
                for matchsticks_to_remove in range(1, min(heap, limit) + 1):
                    new_heaps = heaps[:]
                    new_heaps[i] -= matchsticks_to_remove
                    score, _ = alphabeta(new_heaps, depth - 1, alpha, beta, True, limit)
                    if score < min_score:
                        min_score = score
                        best_move = (i, matchsticks_to_remove)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return min_score, best_move

def main():
    num_heaps = int(input("Enter the number of heaps: "))
    heaps = []
    for i in range(num_heaps):
        heaps.append(int(input(f"Enter the number of matchsticks in Heap {i + 1}: ")))

    limit = int(input("Enter the limit of matchsticks that can be removed in each move: "))

    game = NimGame(heaps)

    while not game.game_over():
        print("Your turn:")
        game.take_turn(limit)
        if game.game_over():
            print("Computer Wins!")
            break

        print("Computer's turn:")
        score, (heap_index, matchsticks) = alphabeta(game.heaps, depth=3, alpha=float('-inf'), beta=float('inf'), is_maximizing=True, limit=limit)
        game.heaps[heap_index] -= matchsticks
        print(f"Computer removes {matchsticks} matchsticks from Heap {heap_index + 1}.")
        if game.game_over():
            print("You Win!")
            break

if __name__ == "_main_":
    main()