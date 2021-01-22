#coding:utf8
import unittest
import pytest
from unittest import mock


from source.env import Cell, Board

VALUES = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
GRID = 3

display = """. . 3 |. 2 . |6 . . 
9 . . |3 . 5 |. . 1 
. . 1 |8 . 6 |4 . . 
------+------+------
. . 8 |1 . 2 |9 . . 
7 . . |. . . |. . 8 
. . 6 |7 . 8 |2 . . 
------+------+------
. . 2 |6 . 9 |5 . . 
8 . . |2 . 3 |. . 9 
. . 5 |. 1 . |3 . . """

class BoardTest(unittest.TestCase):
    """Test Soduku Board"""
    def setUp(self):
        self.board = Board(9, 9, grid=GRID)
        self.board._create(VALUES)

    def test_repr(self):
        self.assertEqual(len(repr(self.board)), len(display))
        self.assertEqual(repr(self.board), display)
    

    def test_board_cell(self):
        for col, value in enumerate("..3.2.6..", 1):
            loc = f"A{col}"
            cell = self.board[loc]
            self.assertEqual(cell.value, value, f"Target col: {col}"
                f" cell:{cell.row}, {cell.column}"
            )

    
    def test_board_iter(self):
        """Test Cell Iterator"""
        for index, (cell, value) in enumerate(zip(self.board, VALUES)):
            self.assertEqual(cell.value, value, f"Cell at {cell.row}, {cell.column}"
                f"Value at {index}"
            )


    def test_board_length(self):
        """Test Total Board Cell"""
        self.assertEqual(len(self.board), self.board.rows * self.board.cols)
        self.board.boxes[0].pop()
        self.assertEqual(len(self.board), self.board.rows * self.board.cols - 1)