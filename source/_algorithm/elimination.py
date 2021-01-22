#coding:utf8
"""
消除法解决数独
"""

from ..env import Board

import math



class Elimination:
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
        self.env = Board(rows, cols, grid)

        if copy:
            self._copy = self._copy_env(self.env)


    @classmethod
    def _copy_env(cls, board):
        """复制环境
        
        复制环境同时修正 cell 中的值，如果数据是数字或者数值字符串，直接保留为字符数值；如果是空格
        或者 '.' 那么替换为空格。其他类型表示 board 中的 Cell 数据值类型不准确
        """
        result = Board(board.rows, board.cols)
        for cell, target in zip(result, board):
            if isinstance(target.value, int):
                cell.value = str(target.value)
            elif isinstance(target.value, str):
                if target.value.isdigit():
                    cell.value = target.value
                elif target.value == "" or target.value == ".":
                    cell.value = []
            else:
                raise ValueError(f"Cell value is not a digit value,"
                                f" get type {type(target.value)}")
        
        return result