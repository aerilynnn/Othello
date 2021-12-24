import math
from tiles import Tiles
from copy import deepcopy


class GameController:
    """Controls the rules of othello game"""
    def __init__(self, WIDTH, HEIGHT, dimension, tiles):
        """
        Attributes
        ----------------------
        WIDTH (int): grid width
        HEIGHT (int): grid height
        dimension (int): dimensionXdimension dimensions of grid
        game_over (boolean): whether game is over or not
        black_tiles (int): number of black tiles on grid
        white_tiles (int): number of white tiles on grid
        num_tiles (int): total number of tiles on grid
        DISTANCE_THRES (int): maximum distance click can be from tile
        turn_tracker (int): number in game
        black (tuple): RGB value of black
        white (tuple): RGB value of white
        green (tuple): RGB value of green
        tiles (object): Tiles object
        CORNER_POSITIONS (list): list of coordinates of all corner positions
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.dimension = dimension
        self.game_over = False
        self.black_tiles = 2
        self.white_tiles = 2
        self.num_tiles = 4
        self.DISTANCE_THRES = 50
        self.turn_tracker = 0
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 100, 0)
        self.tiles = tiles
        self.CORNER_POSITIONS = [[0, 0], [0, self.dimension-1],
                                 [self.dimension-1, 0], [self.dimension-1,
                                 self.dimension-1]]
        self.clone = deepcopy(self)
    def get_distance(self, x1, x2, y1, y2):
        """
        Parameters
        ----------------------
        x1 (int): x1 position
        x2 (int): x2 position
        y1 (int): y1 position
        y2 (int): y2 position

        Returns
        -------------------------
        float

        Finds the distance between two points and
        returns it.
        """
        distance = abs(math.sqrt((x2-x1)**2 + (y2-y1)**2))
        return distance

    def show_legal_moves(self, value):
        """
        Parameters
        ------------------
        value (int): value that is representation of which turn it is

        Returns
        ------------------
        None

        For each turn, finds all legal spots for tile to be placed by
        examining all tiles of opposite color that can be flipped.
        """
        if value % 2 == 0:
            turn_color = self.black
            opposing_color = self.white
        else:
            turn_color = self.white
            opposing_color = self.black

        for i in range(len(self.tiles.tiles)):
            for j in range(len(self.tiles.tiles[i])):
                if [i, j] not in self.CORNER_POSITIONS:  # Can't flip corners
                    if self.tiles.tiles[i][j].fill_color == opposing_color:
                        # Check all square in all 8 directions of tile
                        # Top direction
                        if i in range(1, self.dimension-1):
                            if self.tiles.tiles[i+1][j].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i-1][j].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i-1][j].clickable = True
                                    self.tiles.tiles[i][j].possible_flippers.\
                                        add(self.tiles.tiles[i-1][j])
                                if self.tiles.tiles[i-1][j].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append(i)
                                    for y in range(i, -1, -1):
                                        if self.tiles.tiles[y][j].\
                                                fill_color == opposing_color:
                                            temp_list.append(y)
                                        elif self.tiles.tiles[y][j].\
                                                fill_color == self.green:
                                            for val in temp_list:
                                                self.tiles.tiles[val][j].\
                                                    possible_flippers.add(
                                                        self.tiles.tiles[y][j]
                                                        )
                                            self.tiles.tiles[y][j].clickable =\
                                                True
                                            break
                                        else:
                                            break

                        # Bottom direction
                        if i in range(1, self.dimension-1):
                            if self.tiles.tiles[i-1][j].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i+1][j].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i+1][j].clickable = True
                                    self.tiles.tiles[i][j].possible_flippers.\
                                        add(self.tiles.tiles[i+1][j])
                                if self.tiles.tiles[i+1][j].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append(i)
                                    for y in range(i, self.dimension):
                                        if self.tiles.tiles[y][j].\
                                                fill_color == opposing_color:
                                            temp_list.append(y)
                                        elif self.tiles.tiles[y][j].\
                                                fill_color == self.green:
                                            for val in temp_list:
                                                self.tiles.tiles[val][j].\
                                                    possible_flippers.add(
                                                        self.tiles.tiles[y][j]
                                                        )
                                            self.tiles.tiles[y][j].clickable =\
                                                True
                                            break
                                        else:
                                            break

                        # Left direction
                        if j in range(1, self.dimension-1):
                            if self.tiles.tiles[i][j+1].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i][j-1].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i][j-1].clickable = True
                                    self.tiles.tiles[i][j].possible_flippers.\
                                        add(self.tiles.tiles[i][j-1])
                                if self.tiles.tiles[i][j-1].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append(j)
                                    for y in range(j, -1, -1):
                                        if self.tiles.tiles[i][y].\
                                                fill_color == opposing_color:
                                            temp_list.append(y)
                                        elif self.tiles.tiles[i][y].\
                                                fill_color == self.green:
                                            for val in temp_list:
                                                self.tiles.tiles[i][val].\
                                                    possible_flippers.add(
                                                        self.tiles.tiles[i][y]
                                                        )
                                            self.tiles.tiles[i][y].clickable =\
                                                True
                                            break
                                        else:
                                            break

                        # Right direction
                        if j in range(1, self.dimension-1):
                            if self.tiles.tiles[i][j-1].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i][j+1].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i][j+1].clickable = True
                                    self.tiles.tiles[i][j].\
                                        possible_flippers.add(
                                            self.tiles.tiles[i][j+1]
                                            )
                                if self.tiles.tiles[i][j+1].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append(j)
                                    for y in range(j, self.dimension):
                                        if self.tiles.tiles[i][y].\
                                                fill_color == opposing_color:
                                            temp_list.append(y)
                                        elif self.tiles.tiles[i][y].\
                                                fill_color == self.green:
                                            for val in temp_list:
                                                self.tiles.tiles[i][val].\
                                                    possible_flippers.add(
                                                        self.tiles.tiles[i][y]
                                                        )
                                            self.tiles.tiles[i][y].clickable =\
                                                True
                                            break
                                        else:
                                            break

                        # Top left diagonal direction
                        if i in range(1, self.dimension-1) and \
                                j in range(1, self.dimension-1):
                            if self.tiles.tiles[i+1][j+1].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i-1][j-1].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i-1][j-1].clickable = True
                                    self.tiles.tiles[i][j].possible_flippers.\
                                        add(self.tiles.tiles[i-1][j-1])
                                if self.tiles.tiles[i-1][j-1].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append([i, j])
                                    min_val = min(i, j)
                                    difference = abs(i-j)
                                    for x in range(min_val, -1, -1):
                                        if min_val == i:
                                            tile = self.tiles.\
                                                tiles[x][x+difference]
                                        else:
                                            tile = self.tiles.\
                                                tiles[x+difference][x]
                                        if tile.fill_color == opposing_color:
                                            if tile == self.tiles.\
                                                    tiles[x][x+difference]:
                                                temp_list.append(
                                                    [x, x+difference]
                                                    )
                                            else:
                                                temp_list.append(
                                                    [x+difference, x]
                                                    )
                                        elif tile.fill_color == self.green:
                                            for val in temp_list:
                                                x_val = val[0]
                                                y_val = val[1]
                                                self.tiles.\
                                                    tiles[x_val][y_val].\
                                                    possible_flippers.add(tile)
                                            tile.clickable = True
                                            break
                                        else:
                                            break

                        # Top right diagonal direction
                        if i in range(1, self.dimension-1) and \
                                j in range(1, self.dimension-1):
                            if self.tiles.tiles[i+1][j-1].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i-1][j+1].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i-1][j+1].clickable = True
                                    self.tiles.tiles[i][j].possible_flippers.\
                                        add(self.tiles.tiles[i-1][j+1])
                                if self.tiles.tiles[i-1][j+1].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append([i, j])
                                    total = i+j
                                    if total % 2 == 1:
                                        if total <= 7:
                                            start = i
                                            iterable = range(start, -1, -1)
                                            tag = 1
                                        else:
                                            start = j
                                            iterable = range(start,
                                                             self.dimension)
                                            tag = 2
                                    else:
                                        if total < 7:
                                            start = i
                                            iterable = range(start, -1, -1)
                                            tag = 3
                                        else:
                                            start = j
                                            iterable = range(start,
                                                             self.dimension)
                                            tag = 4
                                    for x in iterable:
                                        if tag == 1 or tag == 3:
                                            tile = self.tiles.tiles[x][total-x]
                                        else:
                                            tile = self.tiles.tiles[total-x][x]
                                        if tile.fill_color == opposing_color:
                                            if tag == 1 or tag == 3:
                                                temp_list.append([x, total-x])
                                            else:
                                                temp_list.append([total-x, x])
                                        elif tile.fill_color == self.green:
                                            for val in temp_list:
                                                x_val = val[0]
                                                y_val = val[1]
                                                self.tiles.\
                                                    tiles[x_val][y_val].\
                                                    possible_flippers.add(tile)
                                            tile.clickable = True
                                            break
                                        else:
                                            break

                        # Bottom left diagonal direction
                        if i in range(1, self.dimension-1) and \
                                j in range(1, self.dimension-1):
                            if self.tiles.tiles[i-1][j+1].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i+1][j-1].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i+1][j-1].clickable = True
                                    self.tiles.tiles[i][j].possible_flippers.\
                                        add(self.tiles.tiles[i+1][j-1])
                                if self.tiles.tiles[i+1][j-1].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append([i, j])
                                    total = i+j
                                    if total % 2 == 1:
                                        if total <= 7:
                                            start = j
                                            iterable = range(start, -1, -1)
                                            tag = 1
                                        else:
                                            start = i
                                            iterable = range(start,
                                                             self.dimension)
                                            tag = 2
                                    else:
                                        if total < 7:
                                            start = j
                                            iterable = range(start, -1, -1)
                                            tag = 3
                                        else:
                                            start = i
                                            iterable = range(start,
                                                             self.dimension)
                                            tag = 4
                                    for x in iterable:
                                        if tag == 1 or tag == 3:
                                            tile = self.tiles.tiles[total-x][x]
                                        else:
                                            tile = self.tiles.tiles[x][total-x]
                                        if tile.fill_color == opposing_color:
                                            if tag == 1 or tag == 3:
                                                temp_list.append([total-x, x])
                                            else:
                                                temp_list.append([x, total-x])
                                        elif tile.fill_color == self.green:
                                            for val in temp_list:
                                                x_val = val[0]
                                                y_val = val[1]
                                                self.tiles.\
                                                    tiles[x_val][y_val].\
                                                    possible_flippers.add(tile)
                                            tile.clickable = True
                                            break
                                        else:
                                            break

                        # Bottom right diagonal direction
                        if i in range(1, self.dimension-1) and \
                                j in range(1, self.dimension-1):
                            if self.tiles.tiles[i-1][j-1].fill_color == \
                                    turn_color:
                                if self.tiles.tiles[i+1][j+1].fill_color == \
                                        self.green:
                                    self.tiles.tiles[i+1][j+1].clickable = True
                                    self.tiles.tiles[i][j].possible_flippers.\
                                        add(self.tiles.tiles[i+1][j+1])
                                if self.tiles.tiles[i+1][j+1].fill_color == \
                                        opposing_color:
                                    temp_list = []
                                    temp_list.append([i, j])
                                    max_val = max(i, j)
                                    difference = abs(i-j)
                                    for x in range(max_val, self.dimension):
                                        if max_val == j:
                                            tile = self.tiles.\
                                                tiles[x-difference][x]
                                        else:
                                            tile = self.tiles.\
                                                tiles[x][x-difference]

                                        if tile.fill_color == opposing_color:
                                            if tile == self.tiles.\
                                                    tiles[x][x-difference]:
                                                temp_list.append([x,
                                                                  x-difference]
                                                                 )
                                            else:
                                                temp_list.append(
                                                    [x-difference, x]
                                                    )
                                        elif tile.fill_color == self.green:
                                            for val in temp_list:
                                                x_val = val[0]
                                                y_val = val[1]
                                                self.tiles.\
                                                    tiles[x_val][y_val].\
                                                    possible_flippers.add(tile)
                                            tile.clickable = True
                                            break
                                        else:
                                            break
        self.clone = deepcopy(self)

    def track_legal_moves(self):
        """
        Checks that each player has at least one legal move to make.
        If one player is out of legal moves switch to next. If both players are
        out of moves then game is over.
        """
        legal_moves = False
        loop_break = False
        for i in range(len(self.tiles.tiles)):
            if loop_break:
                break
            for j in range(len(self.tiles.tiles[i])):
                if self.tiles.tiles[i][j].clickable is True:
                    legal_moves = True
                    loop_break = True
                    break

        if legal_moves is False:
            if self.turn_tracker % 2 == 0:
                color = 1
            else:
                color = 0
            self.show_legal_moves(color)
            legal_moves_2 = False
            loop_break_2 = False
            for i in range(len(self.tiles.tiles)):
                if loop_break_2:
                    break
                for j in range(len(self.tiles.tiles[i])):
                    if self.tiles.tiles[i][j].clickable is True:
                        legal_moves_2 = True
                        loop_break_2 = True
                        break

            if legal_moves_2 is True:
                self.turn_tracker += 1
            else:
                self.game_over = True

        self.clone = deepcopy(self)

    def flip(self, xpos, ypos):
            """
            Parameters
            ---------------------
            xpos (int): x coordinate of position clicked
            ypos (int): y coordinate of position clicked

            Returns
            ----------------------
            None

            Checks if the tile that was just placed has any tiles associated with
            it that when placed cause the other tiles to flip. If that is the case,
            then flips all those tiles associated.
            """
            if self.turn_tracker % 2 == 0:
                turn_color = self.black
                opposing_color = self.white
            else:
                turn_color = self.white
                opposing_color = self.black

            for i in range(len(self.tiles.tiles)):
                for j in range(len(self.tiles.tiles[i])):
                    distance = self.get_distance(xpos, self.tiles.tiles[i][j].x,
                                                ypos, self.tiles.tiles[i][j].y)
                    if distance <= self.DISTANCE_THRES:
                        for x in range(len(self.tiles.tiles)):
                            for y in range(len(self.tiles.tiles[x])):
                                if self.tiles.tiles[x][y].fill_color == turn_color:
                                    if self.tiles.tiles[i][j] in self.tiles.\
                                            tiles[x][y].possible_flippers:
                                        self.tiles.tiles[x][y].fill_color = \
                                            opposing_color
                                        self.tiles.tiles[x][y].stroke_color = \
                                            self.black
                                        if opposing_color == self.black:
                                            self.black_tiles += 1
                                            self.white_tiles -= 1
                                        else:
                                            self.white_tiles += 1
                                            self.black_tiles -= 1

                                        for tile in self.tiles.\
                                                tiles[x][y].possible_flippers:
                                            tile.clickable = False
                                            if tile.fill_color == self.black or \
                                                    tile.fill_color == self.white:
                                                tile.stroke_color = self.black
                                            else:
                                                tile.stroke_color = self.green
                                        self.tiles.tiles[x][y].possible_flippers =\
                                            set()

                                    else:
                                        for tile in self.tiles.tiles[x][y].\
                                                possible_flippers:
                                            tile.clickable = False
                                            tile.stroke_color = self.green
                                        self.tiles.tiles[x][y].possible_flippers =\
                                            set()
            self.clone = deepcopy(self)

    def clone_flip(self, x_pos, y_pos, grid):

        """
        Parameters
        ---------------------
        xpos (int): x coordinate of position clicked
        ypos (int): y coordinate of position clicked
        grid: grid to be manipulated 

        Returns
        ----------------------
        The number of tiles that were flipped and the resulting board 

        Checks if the tile that was just placed has any tiles associated with
        it that when placed cause the other tiles to flip. If that is the case,
        then flips all those tiles associated.
        """
        flip_count = 0
        if self.turn_tracker % 2 == 0:
            turn_color = self.black
            opposing_color = self.white
        else:
            turn_color = self.white
            opposing_color = self.black

        for i in range(len(grid.tiles.tiles)):
            for j in range(len(grid.tiles.tiles[i])):
                distance = self.get_distance(x_pos, grid.tiles.tiles[i][j].x,
                                             y_pos, grid.tiles.tiles[i][j].y)
                if distance <= self.DISTANCE_THRES:
                    for x in range(len(grid.tiles.tiles)):
                        for y in range(len(grid.tiles.tiles[x])):
                            if grid.tiles.tiles[x][y].fill_color == turn_color:
                                if grid.tiles.tiles[i][j] in grid.tiles.\
                                        tiles[x][y].possible_flippers:
                                    grid.tiles.tiles[x][y].fill_color = \
                                        opposing_color
                                    grid.tiles.tiles[x][y].stroke_color = \
                                        self.black
                                    if opposing_color == self.black:
                                        flip_count = flip_count + 1
                                        self.clone.black_tiles += 1
                                        self.clone.white_tiles -= 1
                                    else:
                                        flip_count = flip_count + 1
                                        self.clone.white_tiles += 1
                                        self.clone.black_tiles -= 1

                                    for tile in grid.tiles.\
                                            tiles[x][y].possible_flippers:
                                        tile.clickable = False
                                        if tile.fill_color == self.black or \
                                                tile.fill_color == self.white:
                                            tile.stroke_color = self.black
                                        else:
                                            tile.stroke_color = self.green
                                    grid.tiles.tiles[x][y].possible_flippers =\
                                        set()

                                else:
                                    for tile in grid.tiles.tiles[x][y].\
                                            possible_flippers:
                                        tile.clickable = False
                                        tile.stroke_color = self.green
                                    grid.tiles.tiles[x][y].possible_flippers =\
                                        set()
        return flip_count, grid

    def turn_announcer(self):
        """Prints to terminal whose turn it is"""
        if self.game_over is False:
            if self.turn_tracker % 2 == 0:
                print("IT'S BLACK'S TURN")
            else:
                print("IT'S WHITE'S TURN")

    def update(self):
        """
        If the game is over, makes all tiles unclickable and
        displays to the screen the winner and how many tiles
        each player got.
        """
        if self.game_over is True:
            for i in range(len(self.tiles.tiles)):
                for j in range(len(self.tiles.tiles[i])):
                    self.tiles.tiles[i][j].clickable = False

            fill(255, 255, 0)
            textSize(50)
            if self.black_tiles == self.white_tiles:
                text("IT'S A TIE", self.WIDTH/2 - 140, self.HEIGHT/2)
            elif self.black_tiles > self.white_tiles:
                text("BLACK WINS!", self.WIDTH/2 - 140, self.HEIGHT/2)
            else:
                text("WHITE WINS!", self.WIDTH/2 - 140, self.HEIGHT/2)
            text("Number of black tiles:%d" % self.black_tiles,
                 self.WIDTH/2 - 300, self.HEIGHT/2 + 100)
            text("Number of white tiles:%d" % self.white_tiles,
                 self.WIDTH/2 - 300, self.HEIGHT/2 + 200)