from grid import Grid
from game_controller import GameController
from tiles import Tiles

HEIGHT = 800
WIDTH = 800
dimension = 8

tiles = Tiles(WIDTH, HEIGHT, dimension)
gc = GameController(WIDTH, HEIGHT, dimension, tiles)
grid = Grid(WIDTH, HEIGHT, dimension, gc, tiles)


def test_constructor():
    """Test constructor"""
    assert grid.WIDTH == 800
    assert grid.HEIGHT == 800
    assert grid.dimension == 8
    assert grid.SIZE == 100
    assert grid.tiles == tiles
    assert grid.black == (0, 0, 0)
    assert grid.white == (255, 255, 255)
    assert grid.green == (0, 100, 0)
    assert grid.gc == gc


def test_click():
    """Test click method"""
    gc.turn_tracker = 0
    gc.white_tiles = 10
    gc.black_tiles = 11
    x_pos = 250
    y_pos = 350
    gc.tiles.tiles[3][2].clickable = True
    grid.click(x_pos, y_pos)
    assert gc.tiles.tiles[3][2].fill_color == (0, 0, 0)
    assert gc.white_tiles == 10
    assert gc.black_tiles == 12
    gc.tiles.tiles[0][2].clickable = False
    x_pos = 250
    y_pos = 50
    grid.click(x_pos, y_pos)
    assert gc.tiles.tiles[0][2].fill_color == (0, 100, 0)
    assert gc.white_tiles == 10
    assert gc.black_tiles == 12


def test_update():
    """Test update method"""
    gc.num_tiles = 58
    grid.update()
    assert gc.game_over is False
    gc.num_tiles = 64
    grid.update()
    assert gc.game_over is True
