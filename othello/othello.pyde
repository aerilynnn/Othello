from game_controller import GameController
from tiles import Tiles
from grid import Grid
from computer import Computer

HEIGHT = 800
WIDTH = 800
dimension = 8
background_color = (0, 100, 0)

tiles = Tiles(WIDTH, HEIGHT, dimension)
gc = GameController(WIDTH, HEIGHT, dimension, tiles)
grid = Grid(WIDTH, HEIGHT, dimension, gc, tiles)
computer = Computer(grid, gc)
mouse_moved = False
delay_time = 1500


def setup():
    """Defines intial properties of game"""
    size(WIDTH, HEIGHT)
    background(background_color[0],
               background_color[1],
               background_color[2])


def draw():
    """Draws the board and tiles during each frame"""
    grid.display()
    grid.update()
    gc.turn_announcer()
    gc.track_legal_moves()
    gc.update()


def mousePressed():
    """Handles the event when the mouse is clicked to place a tile or when click happens to trigger computer move"""
    grid.click(mouseX, mouseY)
    gc.flip(mouseX, mouseY)
    #computer.make_random_move()
    #grid.click(computer.random_move[0], computer.random_move[1])
    #gc.flip(computer.random_move[0], computer.random_move[1])

def mouseReleased():
    "Handles the event for when it's the computer's turn following player"
    draw()
    computer.make_move()
    grid.click(computer.move[0], computer.move[1])
    gc.flip(computer.move[0], computer.move[1])
    #computer.minimax_move(grid, 2, True)
    #grid.click(computer.move[0], computer.move[1])
    #gc.flip(computer.move[0], computer.move[1])
