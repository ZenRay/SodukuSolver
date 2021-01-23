#coding:utf8
import pytest
import unittest
from unittest import mock

from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), "../.."))
from source._algorithm import elimination


# @pytest.fixture
# def values():
#     result = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8.' \
#                 '.2.3..9..5.1.3..'
#     return result
    

VALUES = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
class TestElimination(unittest.TestCase):
    def setUp(self) -> None:
        self.env = elimination.Elimination(VALUES)
        return super().setUp()

    
    def test_copy_env_classmethod(self):
        """测试复制环境的方法被调用"""
        elimination.Elimination._copy_env = mock.MagicMock(name='copy')
        elim = elimination.Elimination("113422389")
        elim._copy_env.assert_called_once()


    def test_candidates(self):
        """获取待选数据"""
        a1 = "".join(self.env.candidates("A1"))
        self.assertEqual(a1, "45")
        a2 = "".join(self.env.candidates("A2"))
        self.assertEqual(a2, "4578")

        i9 = "".join(self.env.candidates("I9"))
        self.assertEqual(i9, "2467")