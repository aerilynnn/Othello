from game_controller import GameController
from tiles import Tiles
from grid import Grid

HEIGHT = 800
WIDTH = 800
dimension = 8

tiles = Tiles(WIDTH, HEIGHT, dimension)
gc = GameController(WIDTH, HEIGHT, dimension, tiles)
grid = Grid(WIDTH, HEIGHT, dimension, gc, tiles)


def test_constructor():
    """Test constructor"""
    assert gc.WIDTH == 800
    assert gc.HEIGHT == 800
    assert gc.dimension == 8
    assert gc.game_over is False
    assert gc.black_tiles == 2
    assert gc.white_tiles == 2
    assert gc.num_tiles == 4
    assert gc.DISTANCE_THRES == 50
    assert gc.turn_tracker == 0
    assert gc.black == (0, 0, 0)
    assert gc.white == (255, 255, 255)
    assert gc.green == (0, 100, 0)
    assert gc.tiles == tiles
    assert gc.CORNER_POSITIONS == [
        [0, 0], [0, 7], [7, 0], [7, 7]]


def test_get_distance():
    """Test get_distance method"""
    xpos1 = 250
    ypos1 = 70
    xpos2 = 483
    ypos2 = 234
    distance = gc.get_distance(xpos1, xpos2, ypos1, ypos2)
    assert round(distance, 2) == 284.93


def test_show_legal_moves():
    """Test show_legal_moves method"""
    value = 0
    gc.tiles.tiles[6][1].fill_color = (255, 255, 255)
    gc.tiles.tiles[5][2].fill_color = (255, 255, 255)
    gc.tiles.tiles[2][5].fill_color = (255, 255, 255)
    gc.tiles.tiles[3][5].fill_color = (255, 255, 255)
    gc.tiles.tiles[3][6].fill_color = (255, 255, 255)
    gc.tiles.tiles[2][2].fill_color = (0, 0, 0)

    gc.show_legal_moves(value)
    assert gc.tiles.tiles[7][0].clickable is True
    assert gc.tiles.tiles[3][2].clickable is True
    assert gc.tiles.tiles[2][3].clickable is True
    assert gc.tiles.tiles[5][4].clickable is True
    assert gc.tiles.tiles[4][5].clickable is True
    assert gc.tiles.tiles[5][5].clickable is True
    assert gc.tiles.tiles[1][6].clickable is True
    assert gc.tiles.tiles[3][7].clickable is True
    assert gc.tiles.tiles[0][0].clickable is False
    assert gc.tiles.tiles[5][2].clickable is False
    assert gc.tiles.tiles[4][3].clickable is False


def test_track_legal_moves():
    """Test track_legal_moves method"""
    gc.turn_tracker = 0
    gc.track_legal_moves()
    assert gc.turn_tracker == 0

    for i in range(len(gc.tiles.tiles)):
        for j in range(len(gc.tiles.tiles[i])):
            gc.tiles.tiles[i][j].clickable = False
    gc.turn_tracker = 0
    gc.track_legal_moves()
    assert gc.turn_tracker == 1
    assert gc.game_over is False


def test_flip():
    """Test flip method"""
    gc.turn_tracker = 0
    xpos = 250
    ypos = 350
    grid.click(xpos, ypos)
    gc.flip(xpos, ypos)
    assert gc.tiles.tiles[3][3].fill_color == (255, 255, 255)
    assert gc.tiles.tiles[0][4].fill_color == (0, 100, 0)
    assert gc.tiles.tiles[1][3].fill_color == (0, 100, 0)
    assert gc.tiles.tiles[6][6].fill_color == (0, 100, 0)
