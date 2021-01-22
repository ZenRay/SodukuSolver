#coding:utf8

# row start charater
ROW_START = ord("A")


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


class Board:
    def __init__(self, rows, cols, grid=3):
        """Board Enviroment
        
        """
        self.rows = rows
        self.cols = cols
        self.boxes = []
        self.grid = grid

    def _create(self, values=None):
        """Create Board Box

        If grid values exist, initialize the cell value, otherwise setup None
        """
        assert values is None or self.rows * self.cols == len(values), \
            "Grid length isn't equal with total of the box cell"

        for row in range(self.rows):
            rows = []
            for col in range(self.cols):
                # get cell value
                if values is not None:
                    value = values[0]
                    values = values[1:]
                else:
                    value = None
                
                rows.append(Cell(chr(row + ROW_START), col, value))
                
            # put rows cell into box
            self.boxes.append(rows)

    
    def __repr__(self):
        """Display Box

        Format string of the box, like this:
            . . 3 |. 2 . |6 . . 
            9 . . |3 . 5 |. . 1 
            . . 1 |8 . 6 |4 . . 
            ------+------+------
            . . 8 |1 . 2 |9 . . 
            7 . . |. . . |. . 8 
            . . 6 |7 . 8 |2 . . 
            ------+------+------
            . . 2 |6 . 9 |5 . . 
            8 . . |2 . 3 |. . 9 
            . . 5 |. 1 . |3 . .
        """
        fmt = []
        for i, row in enumerate(self.boxes, 1):
            line = ""
            for index, cell in enumerate(row, 1):
                if index != len(row) and index % 3 == 0:
                    line += f"{cell.value} " + "|"
                else:
                    line += f"{cell.value} "
            fmt.append(line)

            if i % 3 == 0 and i != len(self.boxes):
                fmt.append("+".join(["-" * self.grid * 2] * self.grid))
        return "\n".join(fmt)
