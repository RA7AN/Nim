class NixGame:
    def _init_(self, piles):
        self.piles = piles

    def game_over(self):
        return sum(self.piles) == 0

    def generate_moves(self):
        moves = []
        for i, pile in enumerate(self.piles):
            for j in range(1, pile + 1):
                moves.append((i, j))
        return moves

    def make_move(self, move):
        pile, count = move
        self.piles[pile] -= count

    def undo_move(self, move):
        pile, count = move
        self.piles[pile] += count

    def evaluate(self):
        # Evaluation function for the current game state
        return sum(self.piles)

def minimax_search(game, depth, maximizing_player):
    if depth == 0 or game.game_over():
        return game.evaluate()

    if maximizing_player:
        max_eval = -float('inf')
        for move in game.generate_moves():
            game.make_move(move)
            eval = minimax_search(game, depth - 1, False)
            game.undo_move(move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in game.generate_moves():
            game.make_move(move)
            eval = minimax_search(game, depth - 1, True)
            game.undo_move(move)
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(game, depth):
    best_move = None
    best_eval = -float('inf')
    for move in game.generate_moves():
        game.make_move(move)
        eval = minimax_search(game, depth - 1, False)
        game.undo_move(move)
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def main():
    # Example usage
    piles = [3, 4, 5]
    game = NixGame(piles)
    depth = 3
    while not game.game_over():
        move = get_best_move(game, depth)
        game.make_move(move)
        print("Player makes move:", move)
        print("Piles:", game.piles)
        if game.game_over():
            print("Player wins!")
            break
        move = tuple(int(x) for x in input("Enter your move (pile index, count): ").split())
        game.make_move(move)
        print("Piles:", game.piles)
        if game.game_over():
            print("Computer wins!")

if _name_ == "_main_":
    main()