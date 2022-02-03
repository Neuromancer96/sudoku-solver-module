class SudokuSolver:
    
    @classmethod
    def find_empty(cls, p_sudoku):
        """
        Returns first empty cell, represented with value 0
        or None if no empty cell is found.
            
        Params:
            -- array of arrays of ints
        Return:
            -- tuple of two coordinates or None
        """
    
        for i in range(9):
            for j in range(9):
                if p_sudoku[i][j] == 0:
                    return (i, j)
        
        return None
        
    @classmethod
    def solve(cls, p_sudoku):
        """
        Returns first sudoku solution found or None if there is no solution
        for given pattern.
        
        Params:
            -- array of arrays of ints
        Return:
            -- array of arrays of ints or None
        """

        sudoku = p_sudoku
        cell_tracking = []
        
        # validate given pattern
        if not cls.validate_pattern(p_sudoku):
            return None
        
        # repeat until solution is found or
        # it is clear no solution is possible
        while True:
        
            # find new empty cell
            new_cell = cls.find_empty(sudoku)
            
            if new_cell:
                cell_tracking.append(new_cell) # track new cell
            else:
                return sudoku # solution is complete
                
            # set coordinates, value and possibility to use of last cell
            i, j = cell_tracking[-1]
            current = sudoku[i][j]
            is_possible = False
        
            while not is_possible:
            
                # if next value after current is 10
                # null last tracked cell and throw away its tracking
                # then set new last tracked cell
                # and save its current value
                
                # test +1 because "current" was tested previoulsy
                # and didn't pass
                if current + 1 > 9:
                    
                    # if i can't use any number in the first cell
                    # there is no solution for given pattern
                    if len(cell_tracking) <= 1:
                        return None
                        
                    else:
                        # null that cell and track previous one
                        sudoku[i][j] = 0
                        cell_tracking.pop(-1)
                        
                        # set new tracked value
                        # is no need to false is_possible
                        # it have not been trued yet
                        i, j = cell_tracking[-1]
                        current = sudoku[i][j]
                        
                else:
                
                    # try new value in empty cell
                    is_possible = cls.validate(sudoku, (i, j), current + 1)
                    
                    if is_possible:
                        sudoku[i][j] = current + 1 # use this possible value
                        break
                    else:
                        current += 1 # increment current value
                        
    @classmethod
    def validate(cls, p_sudoku, p_pos, p_val):
        """
        Returns True if value can be used in given position.
        
        Params:
            -- array of arrays of ints
            -- tuple of ints
            -- int
        Return:    
            -- boolean
        """
        r, c = p_pos
    
        # test row
        if p_val in p_sudoku[r]:
            return False
        
        # test col
        if p_val in [p_sudoku[k][c] for k in range(9)]:
            return False
            
        # test subsquare
        firstrow = (r // 3) * 3
        lastrow = firstrow + 3
        firstcol = (c // 3) * 3
        lastcol = firstcol + 3
        
        for i in range(firstrow, lastrow):
            for j in range(firstcol, lastcol):
                if p_sudoku[i][j] == p_val:
                    return False
        
        # if no conflict found, return True
        return True

    @classmethod
    def validate_pattern(cls, p_sudoku):
        """
        Returns True if given pattern is valid.
        Is it used because solve() method can't find conflict between
        preset values, only empty cells.
        
        Params:
            -- array of arrays of ints
        Return:
            -- boolean
        """
        
        # test if every value is between 0 and 9:
        for i in range(9):
            for j in range(9):
                if p_sudoku[i][j] < 0 or p_sudoku[i][j] > 9:
                    return False
        
        # test every value
        for x in range(1, 10):
            for i in range(9):
                # set row and col for test
                row, col = [], []
                
                # fill row and col
                for j in range(9):
                    row.append(p_sudoku[i][j])
                    col.append(p_sudoku[j][i])
                
                # test occurences
                if row.count(x) > 1 or col.count(x) > 1:
                    return False
        
        return True 