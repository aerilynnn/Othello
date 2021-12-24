from grid import Grid
from game_controller import GameController
import random

q_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

class Computer:
    """Class for the computer that plays the game and it's AI"""
    def __init__(self, grid, gamecontroller):
        """
        Attributes
        -------------------
        grid (object): Grid object
        gc (object): Gamecontroller object
        green (tuple): RGB value of green
        possible_moves (list): list of possible moves computer can make
        random_move (list): random move the computer will make where index 0
        is x coordinate and 1 is y coordinate.
        """
        self.grid = grid
        self.gc = gamecontroller
        self.green = (0, 100, 0)
        self.possible_moves = []
        self.move = None
        self.random_move = None
    
    def make_random_move(self):
        """
        #Computer makes move by going through list of legal moves
        #and picking random one.
        """
        if self.gc.game_over is not True:
            if self.gc.turn_tracker % 2 == 0: # Take the place of the human player 
                self.possible_moves = []
                for i in range(len(self.gc.tiles.tiles)):
                    for j in range(len(self.gc.tiles.tiles[i])):
                        if self.gc.tiles.tiles[i][j].fill_color == \
                                self.green and \
                                self.gc.tiles.tiles[i][j].clickable is True:
                            self.possible_moves.append(
                                [self.gc.tiles.tiles[i][j].x,
                                 self.gc.tiles.tiles[i][j].y]
                                 )
                index = random.randrange(0, len(self.possible_moves))
                self.random_move = self.possible_moves[index]
    
    
    def make_move(self):
        """
        Computer makes picks the move with the highest heuristic value. Best first search. 
        """
        if self.gc.game_over is not True:
            if self.gc.turn_tracker % 2 == 1:
                self.move, new_board = self.evaluation_function(self.grid.clone)

    def minimax_move(self, board, depth, maximizing_player):
        """
        Makes a move based off the minimax algorithm.
        """
        if depth == 0: # Base case 
            self.move, new_board = self.evaluation_function(board) # Only evaluate from the current grid/board
        else:
            if maximizing_player:
                best_move = None
                best_score = -99999
                possible_moves = self.get_all_posible_moves(board)
                for move in possible_moves:
                    score, new_board = self.evaluate(move, board)
                    v = self.minimax_move(new_board, depth -1, not maximizing_player)
                    if v > score:
                        best_score = v
                        best_move = move
                return best_score

            else:
                best_score = -99999
                possible_moves = self.get_all_posible_moves(board)
                for move in possible_moves:
                    score, new_board = self.evaluate(move, board)
                    v = self.minimax_move(new_board, depth -1, maximizing_player)
                    if v < best_score:
                        best_score = v
                return best_score

    def q_learning(self):
        """
        Q-learning algorithm for learning agent. 
        """
        gamma = 0.8
        reward_matrix = [
            [4, -3, 2, 2, 2, 2, -3, 4],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [2, -1, 1, 0, 0, 1, -1, 2],
            [2, -1, 0, 0, 0, 0, -1, 2],
            [2, -1, 0, 0, 0, 0, -1, 2],
            [2, -1, 1, 0, 0, 1, -1, 2],
            [-3, -4, -1, -1, -1, -1, -4, -3],
            [4, -3, 2, 2, 2, 2, -3, 4]
        ]
        possible_moves = self.get_all_posible_moves(self.grid)
        max_q = -999999
        x_move = None
        y_move = None
        for move in possible_moves: # Pick the best move, if not a random move
            row = move[0]//100
            col = move[1]//100
            if q_matrix[row][col] > max_q:
                max_q = q_matrix[row][col]
                x_move = row * 100 + 50
                y_move = col * 100 + 50
                move = [x_move, y_move]
        new_grid = self.look_ahead(move, self.grid)
        new_possible_moves = self.get_all_posible_moves(new_grid)
        # Get max q value from possible moves
        for new_move in new_possible_moves:
            new_max_q = -999999
            row = move[0]//100
            col = move[1]//100
            if q_matrix[row][col] > max_q:
                new_max_q = q_matrix[row, col]
        
        q_matrix[move[0], move[1]] = reward_matrix[move[0], move[1]] + gamma * new_max_q
        self.move = move


        
    def evaluation_function(self, board):
        """
        Evaluates the utility of a move based on three things:
        1) The mobility of the move: how many possible moves are there
        2) How many tiles will be gained
        3) Is it a corner spot or no
        """
        # Get all possible current moves
        possible_moves = self.get_all_posible_moves(board)
        # Iterate through each move and evaluate the utility of the move
        max_score = -999
        move = None 
        max_board = None
        for move in possible_moves:
            move_score, new_board = self.evaluate(move, board)
            if move_score > max_score:
                max_score = move_score
                max_move = move
                max_board = new_board
        
        return max_move, max_board

    def get_all_posible_moves(self, grid):
        """
        Returns all possible moves of player based on board state
        """
        possible_moves = []
        for i in range(len(grid.tiles.tiles)):
                    for j in range(len(grid.tiles.tiles[i])):
                        if grid.tiles.tiles[i][j].fill_color == \
                                self.green and \
                                grid.tiles.tiles[i][j].clickable is True:
                            possible_moves.append(
                                [grid.tiles.tiles[i][j].x,
                                 grid.tiles.tiles[i][j].y]
                                 )
        return possible_moves


    def evaluate(self, move, board):
        """
        Evaluates a move.
        """
        total_score = 0
        # Is the move in a corner?
        if move == [150, 150] or [150, 750] or [750, 150] or [750, 750]:
            total_score += 1
        
        # How many possible moves does it give?
        flip_count, new_grid = self.look_ahead(move, board)
        possible_moves = self.get_all_posible_moves(new_grid)
        total_score += 0.9 * len(possible_moves)
        
        # How many tiles were gained as a result?
        total_score += 0.4 * flip_count
        return total_score, new_grid
    
    def look_ahead(self, move, board):
        """
        Applies a move to the current state of the board and returns the new state of the board

        Returns:
        Grid object 
        """
        board = board.clone_click(move[0], move[1], board)
        flip_count, new_board = self.gc.clone_flip(move[0], move[1], board) # Pass in the cloned grid because we don't actually want to update the original board
        return flip_count, new_board # Return the new board 

