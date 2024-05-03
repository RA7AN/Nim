class NimGame:
    def __init__(self, piles):
        self.piles = piles

    def game_over(self):
        return all(pile == 0 for pile in self.piles)

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
        return sum(self.piles)

def minimax(game, depth, is_maximizer):
    if game.game_over() or depth == 0:
        return game.evaluate()

    if is_maximizer:
        max_eval = float('-inf')
        for move in game.generate_moves():
            game.make_move(move)
            eval = minimax(game, depth - 1, False)
            game.undo_move(move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in game.generate_moves():
            game.make_move(move)
            eval = minimax(game, depth - 1, True)
            game.undo_move(move)
            min_eval = min(min_eval, eval)
        return min_eval

# Sample instance of Nim game
piles = [3, 4, 5]
game = NimGame(piles)

# Drawing the state space tree
# Since the state space tree can be quite large, I'll provide a textual representation
# representing the moves and evaluation values at each node.
def draw_state_space(game, depth, is_maximizer, prefix=""):
    if depth == 0 or game.game_over():
        print(prefix + "Evaluation:", game.evaluate())
        return
    if is_maximizer:
        print(prefix + "Maximizer's Turn")
    else:
        print(prefix + "Minimizer's Turn")
    for move in game.generate_moves():
        game.make_move(move)
        draw_state_space(game, depth - 1, not is_maximizer, prefix + "\t")
        game.undo_move(move)

print("State Space Tree:")
draw_state_space(game, 2, True)
