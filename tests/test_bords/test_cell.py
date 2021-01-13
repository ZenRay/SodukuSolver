#coding:utf8
import unittest
import pytest
from unittest import mock


from source.board import Cell

class CellTest(unittest.TestCase):
    """Test Board Cell"""
    def setUp(self) -> None:
        self.cell = Cell("A", 1, 9)

    def test_property(self):
        """Test Cell Property"""
        self.assertEqual(self.cell.row, "A")
        self.assertEqual(self.cell.column, 1)
        self.assertEqual(self.cell.value, 9)

    def test_repr(self):
        cell = self.cell
        value = f"<Cell({cell.row}, {cell.column}) {cell.value} at {hex(id(cell))}/>"
        self.assertEqual(repr(self.cell), value)


    def test_print(self):
        self.assertEqual(str(self.cell), "| 9 |")


    def test_validcheck(self):
        """Cell Value Valid Status"""
        obj = mock.Mock()
        obj.valid.side_effect = lambda cell, options: cell.value not in options

        self.assertTrue(obj.valid(self.cell, [0, 1, 3]))
        self.assertFalse(obj.valid(self.cell, [1, 9, 2]))
        self.assertTrue(self.cell._valid(12, [0, 1, 3]))
        self.assertFalse(self.cell._valid(12, [0, 12, 3]))