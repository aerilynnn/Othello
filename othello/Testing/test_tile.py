from tile import Tile


def test_constructor():
    """Test constructor"""
    my_tile = Tile(0, 0, 0.90, (0, 100, 0), (100, 0, 0), False)
    assert my_tile.x == 0
    assert my_tile.y == 0
    assert my_tile.dot_size == 0.90
    assert my_tile.stroke_color == (100, 0, 0)
    assert my_tile.fill_color == (0, 100, 0)
    assert my_tile.clickable is False
    assert my_tile.possible_flippers == set()
