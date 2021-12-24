

class Tile:
    """ A class representing a tile in Othello"""
    def __init__(self, x, y, dot_size, fill_color, stroke_color, clickable):
        """
        Attributes
        -----------------------
        dot_size (int): tile size
        fill_color (tuple): color of tile
        stroke_color (tuple): stroke color of tile
        x (int): x coordinate of tile
        y (int): y coordinate of tile
        clickable (boolean): whether or not tile can be clicked
        possible_flippers (set): list of tiles that when flipped will
        flip the color of the tile that list belonds to
        """
        self.dot_size = dot_size
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.x = x
        self.y = y
        self.clickable = clickable
        self.possible_flippers = set()

    def display(self, x, y, width, height, fill_color, stroke_color):
        """Displays the tile as follows"""
        stroke(stroke_color[0], stroke_color[1], stroke_color[2])
        fill(fill_color[0], fill_color[1], fill_color[2])
        ellipse(x, y, width, height)
