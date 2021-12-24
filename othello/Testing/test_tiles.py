from tiles import Tiles


def test_constructor():
    """Test constructor"""
    tiles = Tiles(800, 800, 8)
    assert tiles.WIDTH == 800
    assert tiles.HEIGHT == 800
    assert tiles.dimension == 8
    assert tiles.SIZE == 100
    assert tiles.SIZE_PERCENTAGE == 0.9
    assert tiles.NUM_MIDDLE_TILES == 4
    assert tiles.green == (0, 100, 0)
    assert tiles.black == (0, 0, 0)
    assert tiles.white == (255, 255, 255)

    assert len(tiles.tiles[0]) == 8
    assert tiles.tiles[0][0].fill_color == (0, 100, 0)
    assert tiles.tiles[0][0].stroke_color == (0, 100, 0)
    assert len(tiles.tiles[1]) == 8
    assert len(tiles.tiles[2]) == 8
    assert len(tiles.tiles[3]) == 8
    assert tiles.tiles[3][3].fill_color == (255, 255, 255)
    assert tiles.tiles[3][4].fill_color == (0, 0, 0)
    assert len(tiles.tiles[4]) == 8
    assert len(tiles.tiles[5]) == 8
    assert len(tiles.tiles[6]) == 8
    assert tiles.tiles[6][5].fill_color == (0, 100, 0)
    assert len(tiles.tiles[7]) == 8
    assert len(tiles.middle_tiles) == 4


def test_find_middle_tiles():
    """Test find_middle_tiles method"""
    tiles = Tiles(800, 800, 8)
    assert (350, 350) in tiles.middle_tiles
    assert (350, 450) in tiles.middle_tiles
    assert (450, 350) in tiles.middle_tiles
    assert (450, 450) in tiles.middle_tiles


def test_create_tiles():
    """Test create_tiles method"""
    tiles = Tiles(800, 800, 8)
    assert len(tiles.tiles[0]) == 8
    assert tiles.tiles[0][0].fill_color == (0, 100, 0)
    assert tiles.tiles[0][0].stroke_color == (0, 100, 0)
    assert len(tiles.tiles[1]) == 8
    assert len(tiles.tiles[2]) == 8
    assert len(tiles.tiles[3]) == 8
    assert tiles.tiles[3][3].fill_color == (255, 255, 255)
    assert tiles.tiles[3][4].fill_color == (0, 0, 0)
    assert len(tiles.tiles[4]) == 8
    assert len(tiles.tiles[5]) == 8
    assert len(tiles.tiles[6]) == 8
    assert tiles.tiles[6][5].fill_color == (0, 100, 0)
    assert len(tiles.tiles[7]) == 8
