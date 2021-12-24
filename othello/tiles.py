from tile import Tile

class Tiles:
    """Class representing the collection of all tiles in Othello"""
    def __init__(self, WIDTH, HEIGHT, dimension):
        """
        Attributes
        -------------------
        WIDTH (int): grid width
        HEIGHT (int): grid height
        dimension (int): dimensionXdimension dimensions of grid
        SIZE (int): size of each box on grid
        SIZE_PERCENTAGE (int): percentage of each box to be filled by tile
        middle_tiles (list): list of coordinates of middle tile objects
        black (tuple): RGB value of black
        white (tuple): RGB value of white
        green (tuple): RGB value of green
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.dimension = dimension
        self.SIZE = self.WIDTH//self.dimension
        self.SIZE_PERCENTAGE = 0.9
        self.tiles = []
        self.NUM_MIDDLE_TILES = 4
        self.middle_tiles = []
        self.green = (0, 100, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        self.find_middle_tiles()
        self.create_tiles()

    def find_middle_tiles(self):
        """Finds the x, y position of the 4 middle tiles"""
        for x in range(self.WIDTH//2-self.SIZE//2,
                       self.WIDTH//2+self.SIZE//2+1, self.SIZE):
            for y in range(self.HEIGHT//2-self.SIZE//2,
                           self.HEIGHT//2+self.SIZE//2+1, self.SIZE):
                self.middle_tiles.append((x, y))

    def create_tiles(self):
        """Creates all tiles and populates tiles list"""
        temp_list = []
        count = 0
        for column in range(self.SIZE//2, self.WIDTH, self.SIZE):
            for row in range(self.SIZE//2, self.WIDTH, self.SIZE):
                position = (row, column)
                if position in self.middle_tiles:
                    count += 1
                    if count == 1:
                        color = self.white
                    elif count == 4:
                        color = self.white
                    else:
                        color = self.black
                    stroke_color = self.black
                    clickable = False
                else:
                    color = self.green
                    stroke_color = self.green
                    clickable = False
                temp_list.append(Tile(position[0], position[1],
                                 self.SIZE*self.SIZE_PERCENTAGE,
                                 color, stroke_color, clickable))

        for i in range(0, len(temp_list), self.dimension):
            self.tiles.append(temp_list[i:i+self.dimension])

    def display(self):
        """Displays all tiles in tiles"""
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                self.tiles[i][j].display(
                    self.tiles[i][j].x, self.tiles[i][j].y,
                    self.tiles[i][j].dot_size, self.tiles[i][j].dot_size,
                    self.tiles[i][j].fill_color, self.tiles[i][j].stroke_color)
