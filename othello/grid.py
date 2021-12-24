from tiles import Tiles
from game_controller import GameController
from copy import deepcopy


class Grid:
    """Represents a grid in the game of othello"""
    def __init__(self, WIDTH, HEIGHT, dimension, gamecontroller, tiles):
        """
        Attributes
        -------------------
        WIDTH (int): grid width
        HEIGHT (int): grid height
        dimension (int): dimensionXdimension dimensions of grid
        SIZE (int): size of each box on grid
        tiles (object): Tiles object
        black (tuple): RGB value of black
        white (tuple): RGB value of white
        green (tuple): RGB value of green
        gc (object): Gamecontroller object
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.dimension = dimension
        self.SIZE = self.WIDTH//self.dimension
        self.tiles = tiles
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 100, 0)
        self.gc = gamecontroller
        self.clone = deepcopy(self)

    def draw_lines(self):
        """Draws lines of the grid"""
        strokeWeight(3)
        stroke(self.black[0], self.black[1], self.black[2])
        for x in range(self.SIZE, self.WIDTH, self.SIZE):
            line(x, 0, x, self.HEIGHT)
        for y in range(self.SIZE, self.WIDTH, self.SIZE):
            line(0, y, self.WIDTH, y)

    def click(self, xpos, ypos):
        """
        Parameters
        ---------------------------
        xpos (int/float): x position on grid clicked
        ypos (int/float): y position on grid clicked

        Returns
        ------------------
        None

        Updates the grid with tiles as user/computer clicks
        """
        for i in range(len(self.tiles.tiles)):
            for j in range(len(self.tiles.tiles[i])):
                distance = self.gc.get_distance(xpos, self.tiles.tiles[i][j].x,
                                                ypos, self.tiles.tiles[i][j].y)
                if self.tiles.tiles[i][j].clickable is True:
                    if distance <= self.gc.DISTANCE_THRES:
                        self.gc.turn_tracker += 1
                        if self.gc.turn_tracker % 2 == 1:
                            self.tiles.tiles[i][j].fill_color = self.black
                            self.gc.black_tiles += 1
                        else:
                            self.tiles.tiles[i][j].fill_color = self.white
                            self.gc.white_tiles += 1
                        self.tiles.tiles[i][j].stroke_color = self.black
                        self.tiles.tiles[i][j].clickable = False
                        self.gc.num_tiles += 1
        self.clone = deepcopy(self)

    def clone_click(self, xpos, ypos, board):
        """
        Parameters
        ---------------------------
        xpos (int/float): x position on grid clicked
        ypos (int/float): y position on grid clicked

        Returns
        ------------------
        Returns the new board 

        Updates the cloned grid with tiles as user/computer clicks
        """
        for i in range(len(board.tiles.tiles)):
            for j in range(len(board.tiles.tiles[i])):
                distance = self.clone.gc.get_distance(xpos, board.tiles.tiles[i][j].x,
                                                ypos, board.tiles.tiles[i][j].y)
                if board.tiles.tiles[i][j].clickable is True:
                    if distance <= self.clone.gc.DISTANCE_THRES:
                        board.gc.turn_tracker += 1
                        if board.gc.turn_tracker % 2 == 1:
                            board.tiles.tiles[i][j].fill_color = self.clone.black
                            board.gc.black_tiles += 1
                        else:
                            board.tiles.tiles[i][j].fill_color = self.clone.white
                            board.gc.white_tiles += 1
                        board.tiles.tiles[i][j].stroke_color = self.clone.black
                        board.tiles.tiles[i][j].clickable = False
                        board.gc.num_tiles += 1
        return board

    def update(self):
        """Checks if the grid is all filled up with tiles
        and updates legal moves on grid"""
        self.gc.show_legal_moves(self.gc.turn_tracker)
        if self.gc.num_tiles == (self.dimension)**2:
            self.gc.game_over = True
        self.clone = deepcopy(self)


    def display(self):
        """Displays grid lines and tiles on grid"""
        self.draw_lines()
        self.tiles.display()
