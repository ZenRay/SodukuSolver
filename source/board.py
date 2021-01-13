#coding:utf8


class Cell:
    def __init__(self, row, column, value=None):
        """Board Cell

        """
        self.row = row
        self.column = column
        self.value = value if value is not None else ""

    
    def __repr__(self) -> str:
        id_ = hex(id(self))
        row = self.row
        column = self.column
        value = self.value

        format = f"<Cell({row}, {column}) {value} at {id_}/>"

        return format

    
    def __str__(self) -> str:
        value = "{:^3d}".format(self.value)

        format = f"|{value}|"

        return format

    
    def _valid(self, value, filter):
        """检查 Cell 的值有效性
        
        判断 value 是否在 filter 中，表示 value 不能取 filter 中的数据值。因此如果 value 
        在 filter 中，那么返回 False，反之取 True
        """
        return value not in filter