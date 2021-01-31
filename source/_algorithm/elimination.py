#coding:utf8
"""
消除法解决数独
"""

from ..env import Board, ROW_START
from collections import defaultdict
from copy import deepcopy
import time

import math



class Elimination:
    """ 
    该方法是直接参考 消除法中的思路:
    candidates: 编列 board，消除待选项中多余的值
    update: 更新待选项中列表只有一个元素的 cell
    redue: 循环更新结果，确保每批次都不能再次更新之后传递出结果
    search: 递归更新结果，确保结果满足条件
    """
    def __init__(self, values, *, rows=None, cols=None, copy=True) -> None:
        """初始化对象

        根据行列是否同时申明确定创建数独需要的 Board，缺少其中一个时提示异常。'copy' 表示
        是否需要创建一个备份环境，默认是可以直接创建一个备份环境

        Args:
        --------
        values: str, 数独需要的字符串数据值
        rows, cols: int, 数独需要的行列长度，默认为 None
        copy: bool, 申明是否需要复制一个 Board，默认是复制。其目的是用于后面比较数据数据
        """
        # 不存在行列申明时，直接取平方根；行列只有单参数时报异常
        if rows is None and cols is None:
            rows = math.sqrt(len(values))
            cols = rows
        elif rows is not None and cols is not None:
            pass
        else:
            miss = "rows" if rows is None else "cols"
            raise Exception(f"Arguments '{miss}' lost")
        
        # 创建环境
        rows, cols, grid = int(rows), int(cols), int(math.sqrt(rows))
        env = Board(rows, cols, grid)
        env._create(values)
        
        self.env = self._copy_env(env)
        if copy:
            self._copy = self._copy_env(env)
        else:
            self._copy = None

        self.solutions = []

    @classmethod
    def _copy_env(cls, board):
        """复制环境
        
        复制环境同时修正 cell 中的值，如果数据是数字或者数值字符串，直接保留为字符数值；如果是空格
        或者 '.' 那么替换为空格。其他类型表示 board 中的 Cell 数据值类型不准确
        """
        result = Board(board.rows, board.cols, board.grid)
        result._create()

        for cell, target in zip(result, board):
            
            cell.grid = target.grid
            if isinstance(target.value, int):
                cell.value = str(target.value)
            elif isinstance(target.value, str):
                if target.value.isdigit():
                    cell.value = target.value
                elif target.value == "" or target.value == ".":
                    cell.value = [str(i) for i in range(1, 10)]
            else:
                raise ValueError(f"Cell value is not a digit value,"
                                f" get type {type(target.value)}")
        
        return result


    def candidates(self, board):
        """删除非待选数值
        """
        solved = [(f"{cell.row}{cell.column}", cell.grid) for cell in board if len(cell.value) == 1]
        for loc, grid in solved:
            value = board[loc].value
        
            peers = set(board.row_keys[loc[0]] + board.column_keys[loc[1]] + board.grid_keys[tuple(grid)]) - set([loc])
            for peer in peers:
                if value in board[peer].value and isinstance(board[peer].value, list):
                    board[peer].value.remove(value)
        return board


    def update(self, board):
        """更新结果
        
        """
        for cell in board:
            if isinstance(cell.value, list) and len(cell.value) == 1:
                cell.value = cell.value[0]
            
            # 更新 env 值
            if isinstance(cell.value, str) and cell.value.isdigit():
                self.env[f"{cell.row}{cell.column}"].value = cell.value
        return board


    def reduce(self, board):
        solved = [f"{cell.row}{cell.column}" for cell in board if len(cell.value) == 1]
        stalled = False
        while not stalled:
            solved_before = len([cell for cell in board if len(cell.value) == 1])
            board = self.candidates(board)
            board = self.update(board)
            solved_after = len([cell for cell in board if len(cell.value) == 1])

            stalled = solved_before == solved_after

            if len([cell for cell in board if not cell.value]):
                return False
        return board


    def search(self, board):
        board = self.reduce(board)
        if not board:
            return 
        
        if all(len(cell.value) == 1 for cell in board):
            return board


        length, loc = min((len(cell.value), f"{cell.row}{cell.column}") for cell in board if len(cell.value) > 1)
        for value in board[loc].value:
            new_board = deepcopy(board)
            new_board[loc].value = value

            attempt = self.search(new_board)
            if attempt:
                return  attempt
            
