nodes_explored_minimax = 0
nodes_explored_alphabeta = 0

def evaluate_game_state(state):
    """Evaluate the current game state."""
    return sum(state)

def min_value(state, alpha, beta):
    """Minimizer function for alpha-beta pruning."""
    global nodes_explored_minimax
    nodes_explored_minimax += 1
    
    if evaluate_game_state(state) == 0:
        return 1  # Max wins
    for i in range(len(state)):
        if state[i] > 0:
            for j in range(1, state[i] + 1):
                new_state = state[:]
                new_state[i] -= j
                nodes_explored_minimax += 1
                if max_value(new_state, alpha, beta) == -1:
                    return -1
                beta = min(beta, max_value(new_state, alpha, beta))
                if beta <= alpha:
                    return beta
    return beta

def max_value(state, alpha, beta):
    """Maximizer function for alpha-beta pruning."""
    global nodes_explored_minimax
    nodes_explored_minimax += 1
    
    if evaluate_game_state(state) == 0:
        return -1  # Min wins
    for i in range(len(state)):
        if state[i] > 0:
            for j in range(1, state[i] + 1):
                new_state = state[:]
                new_state[i] -= j
                nodes_explored_minimax += 1
                if min_value(new_state, alpha, beta) == 1:
                    return 1
                alpha = max(alpha, min_value(new_state, alpha, beta))
                if beta <= alpha:
                    return alpha
    return alpha

def alphabeta_decision(state):
    """Decision function using alpha-beta pruning."""
    global nodes_explored_alphabeta
    alpha = float("-inf")
    beta = float("inf")
    for i in range(len(state)):
        if state[i] > 0:
            for j in range(1, state[i] + 1):
                new_state = state[:]
                new_state[i] -= j
                nodes_explored_alphabeta += 1
                if min_value(new_state, alpha, beta) == 1:
                    return i, j
                alpha = max(alpha, min_value(new_state, alpha, beta))

def play_nims():
    """Play the Nim game."""
    global nodes_explored_minimax, nodes_explored_alphabeta
    state = [3, 4, 5]  # Initial state of the game
    print("Starting state:", state)
    while evaluate_game_state(state) > 0:
        print("Player's turn")
        row, stones = map(int, input("Enter row and number of stones to remove (e.g., '1 2'): ").split())
        state[row - 1] -= stones
        print("State after player's move:", state)
        if evaluate_game_state(state) == 0:
            print("Player wins!")
            break
        print("Computer's turn")
        row, stones = alphabeta_decision(state)
        state[row] -= stones
        print("State after computer's move:", state)
        if evaluate_game_state(state) == 0:
            print("Computer wins!")
            break
    print("Nodes explored by Minimax:", nodes_explored_minimax)
    print("Nodes explored by Alpha-beta pruning:", nodes_explored_alphabeta)
    print("Reduced nodes explored:", nodes_explored_minimax - nodes_explored_alphabeta)

play_nims()
