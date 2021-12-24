from file_handler import FileHandler

"""
Uses test_scores.txt to run tests on file with things already in it and
scores.txt to test on empty files. Test module is meant to run only ONCE
as each time it is run, new things are appened to test_scores.txt.
Reset .txt files to original version if test is run more than once.
"""


def test_open_and_read_file():
    """Test open_and_read_file method"""
    file_as_list = FileHandler.open_and_read('test_scores.txt')
    assert file_as_list == ['Aerilynn 100\n', 'John 99\n', 'Luis 40\n',
                            'Penelope 23\n', 'Jean Luc Picard 80\n']
    file_as_list = FileHandler.open_and_read('scores.txt')
    assert file_as_list == []


def test_compare_all_values():
    """Test compare_all_values method"""
    new_score = "Winner 1000\n"
    file_as_list = file_as_list = FileHandler.open_and_read('test_scores.txt')
    FileHandler.compare_all_values(file_as_list, new_score)
    assert file_as_list == ["Winner 1000\n", 'Aerilynn 100\n', 'John 99\n',
                            'Luis 40\n', 'Penelope 23\n',
                            'Jean Luc Picard 80\n']
    new_score = "Aerilynn2 100\n"
    file_as_list = file_as_list = FileHandler.open_and_read('test_scores.txt')
    FileHandler.compare_all_values(file_as_list, new_score)
    assert file_as_list == ["Aerilynn2 100\n", 'Aerilynn 100\n', 'John 99\n',
                            'Luis 40\n', 'Penelope 23\n',
                            'Jean Luc Picard 80\n']
    new_score = "Loser 0\n"
    file_as_list = file_as_list = FileHandler.open_and_read('test_scores.txt')
    FileHandler.compare_all_values(file_as_list, new_score)
    assert file_as_list == ['Aerilynn 100\n', 'John 99\n',
                            'Luis 40\n', 'Penelope 23\n',
                            'Jean Luc Picard 80\n', 'Loser 0\n']
    new_score = "nothing 343\n"
    file_as_list = file_as_list = FileHandler.open_and_read('scores.txt')
    FileHandler.compare_all_values(file_as_list, new_score)
    assert file_as_list == []


def test_overwrite_txt_file():
    """Test overwrite_txt_file method"""
    new_score = "Winner 1000\n"
    file_as_list = FileHandler.open_and_read('test_scores.txt')
    FileHandler.compare_all_values(file_as_list, new_score)
    FileHandler.overwrite_txtfile('test_scores.txt', file_as_list, new_score)
    file_as_list = FileHandler.open_and_read('test_scores.txt')
    assert file_as_list == ["Winner 1000\n", 'Aerilynn 100\n', 'John 99\n',
                            'Luis 40\n', 'Penelope 23\n',
                            'Jean Luc Picard 80\n']

    new_score = "nothing 22\n"
    original_list = FileHandler.open_and_read('scores.txt')
    new_list = FileHandler.compare_all_values(original_list, new_score)
    FileHandler.overwrite_txtfile('scores.txt', new_list, new_score)
    new_file_as_list = FileHandler.open_and_read('scores.txt')
    assert new_file_as_list == ["nothing 22\n"]
