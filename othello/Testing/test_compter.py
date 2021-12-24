from computer import Computer
from grid import Grid
from game_controller import GameController
from tiles import Tiles

HEIGHT = 800
WIDTH = 800
dimension = 8

tiles = Tiles(WIDTH, HEIGHT, dimension)
gc = GameController(WIDTH, HEIGHT, dimension, tiles)
grid = Grid(WIDTH, HEIGHT, dimension, gc, tiles)
computer = Computer(grid, gc)


def test_constructor():
    """Test constructor"""
    assert computer.grid == grid
    assert computer.gc == gc
    assert computer.green == (0, 100, 0)
    assert computer.possible_moves == []
    assert computer.random_move is None


def test_make_move():
    """Test make_move method"""
    gc.turn_tracker = 0
    computer.make_move()
    assert computer.possible_moves == []
    assert computer.random_move is None

    gc.turn_tracker = 1
    gc.tiles.tiles[0][7].fill_color = computer.green
    gc.tiles.tiles[0][7].clickable = True
    gc.tiles.tiles[3][1].fill_color = computer.green
    gc.tiles.tiles[3][1].clickable = True
    gc.tiles.tiles[5][2].fill_color = computer.green
    gc.tiles.tiles[5][2].clickable = False
    computer.make_move()
    assert [gc.tiles.tiles[0][7].x, gc.tiles.tiles[0][7].y] in \
        computer.possible_moves
    assert [gc.tiles.tiles[3][1].x, gc.tiles.tiles[3][1].y] in \
        computer.possible_moves
    assert len(computer.random_move) == 2
    assert [gc.tiles.tiles[3][1].x, gc.tiles.tiles[3][1].y] or \
        [gc.tiles.tiles[0][7].x, gc.tiles.tiles[0][7].y] in \
        computer.random_move
