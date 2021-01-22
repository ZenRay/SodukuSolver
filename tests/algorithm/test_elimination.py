#coding:utf8
import re
import pytest
import unittest
from unittest import mock

from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), "../.."))
from source._algorithm import elimination



class TestElimination(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    
    def test_copy_env_classmethod(self):
        """测试复制环境的方法被调用"""
        elimination.Elimination._copy_env = mock.MagicMock(name='copy')
        elim = elimination.Elimination("1134223")
        elim._copy_env.assert_called_once()
