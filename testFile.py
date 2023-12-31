from lab04 import solveMaze


def test_maze():
    maze = [
        ['+', '+', '+', '+', 'G', '+'],
        ['+', ' ', '+', ' ', ' ', '+'],
        ['+', ' ', ' ', ' ', '+', '+'],
        ['+', ' ', '+', '+', ' ', '+'],
        ['+', ' ', ' ', ' ', ' ', '+'],
        ['+', '+', '+', '+', '+', '+']]
    assert solveMaze(maze, 4, 4) == True
    assert maze == [
        ['+', '+', '+', '+', 'G', '+'],
        ['+', 8, '+', 11, 12, '+'],
        ['+', 7, 9, 10, '+', '+'],
        ['+', 6, '+', '+', 2, '+'],
        ['+', 5, 4, 3, 1, '+'],
        ['+', '+', '+', '+', '+', '+']]


def test_maze2():
    a = [
        ['+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+'],
        ['+', ' ', ' ', ' ', '+', '+'],
        ['G', ' ', '+', '+', ' ', '+'],
        ['+', ' ', ' ', ' ', ' ', '+'],
        ['+', '+', '+', '+', '+', '+']]

    assert solveMaze(a, 4, 4) == True
    assert a == [
        ['+', '+', '+', '+', '+', '+'],
        ['+', '+', '+', '+', '+', '+'],
        ['+', ' ', ' ', ' ', '+', '+'],
        ['G', 6, '+', '+', 2, '+'],
        ['+', 5, 4, 3, 1, '+'],
        ['+', '+', '+', '+', '+', '+']]


def test_maze3():
    b = [
        ['+', '+', '+', '+', '+'],
        ['+', ' ', '+', ' ', '+'],
        ['+', ' ', '+', ' ', '+'],
        ['+', ' ', '+', ' ', '+'],
        ['+', '+', '+', '+', '+']]

    assert solveMaze(b, 3, 3) == False
    assert b == [
        ['+', '+', '+', '+', '+'],
        ['+', ' ', '+', 3, '+'],
        ['+', ' ', '+', 2, '+'],
        ['+', ' ', '+', 1, '+'],
        ['+', '+', '+', '+', '+']]
