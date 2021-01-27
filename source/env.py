#coding:utf8

# row start charater
ROW_START = ord("A")


class Cell:
    def __init__(self, row, column, value=None):
        """Board Cell

        """
        self.row = row
        self.column = str(column)
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


    def __contains__(self, items):
        """检查值限定在确认的范围
        
        examples:
        ------------
        >>> cell = Cell("A", 1, 8)
        >>> [0, 2, 7] in cell
            False
        >>> [0, 8] in cell
            True
        """
        return not self._valid(self.value, items)

class Board:
    """Board Enviroment

    Board enviroment contain cells. The first cell index is 'A1', which columns value
    starts with '1', row value starts with 'A'.

    There are some properties:
    rows: total lines
    cols: total colums
    boxes: board env stores cells
    grid: grid cells in env, where is the small env contains with 'grid' * 'grid'
    """
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
        for row in range(1, self.rows + 1):
            rows = []
            for col in range(1, self.cols + 1):
                # get cell value
                if values is not None:
                    value = values[0]
                    values = values[1:]
                else:
                    value = None
                cell = Cell(chr(row + ROW_START - 1), col, value)

                cell.grid = [(row - 1) // self.grid, (col-1) // self.grid]
                rows.append(cell)
                
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


    def __getitem__(self, loc):
        """Extract Location Value
        
        """
        row = ord(loc[0]) % ROW_START
        col = int(loc[1])
        if col < 1:
            raise ValueError(f"Column value must be over 1 at board env, but get{col}")

        return self.boxes[row][col - 1]


    def __iter__(self):
        for row in self.boxes:
            for cell in row:
                yield cell

        
    def __len__(self):
        """Get Cell Number"""
        return sum(len(row) for row in self.boxes)