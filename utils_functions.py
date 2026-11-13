from constants import (
    GRID_ROW, GRID_COL, SQUARE_SIZE,  OFFSET_X, OFFSET_Y
)

# center = offset + which square + center in square
def center(position):
    row, col = position
    cx = OFFSET_X + col * SQUARE_SIZE + SQUARE_SIZE // 2
    cy = OFFSET_Y + row * SQUARE_SIZE + SQUARE_SIZE // 2
    return cx, cy


def pixels_to_cells(pixels):
    mx, my = pixels

    row = (my - OFFSET_Y) // SQUARE_SIZE
    col = (mx - OFFSET_X) // SQUARE_SIZE
    
    if 0 <= row < GRID_ROW and 0 <= col < GRID_COL:
        return row, col
    return None

def is_adjacent(current_position, new_position):
    curr_row, curr_col = current_position
    new_row, new_col = new_position
    row_diff = abs(new_row - curr_row)
    col_diff = abs(new_col - curr_col)
    
    return row_diff + col_diff == 1

def get_legal_moves(current_position):
    curr_row, curr_col = current_position
    
    # TOP LEFT
    if curr_row == 0 and curr_col == 0:
        pass
    
    # TOP 
    if curr_row == 0 and curr_col != 0:
        pass
    
    # TOP RIGHT
    if curr_row == 0 and curr_col == GRID_COL - 1:
        pass
    
    # BOTTOM LEFT
    if curr_row == GRID_ROW - 1 and curr_col == 0:
        pass
    
    # BOTTOM 
    if curr_row == GRID_ROW - 1 and curr_col != 0:
        pass
    
    # BOTTOM RIGHT
    if curr_row == GRID_ROW - 1 and curr_col == GRID_COL - 1:
        pass
    
    # RIGHT
    if curr_row == GRID_ROW - 1 and curr_col == GRID_COL - 1:
        pass
    
    # LEFT
    
    
    legal_moves = [
        (curr_row + 1, curr_col),
        (curr_row - 1, curr_col),
        (curr_row, curr_col + 1),
        (curr_row, curr_col - 1)
    ]
    
    return legal_moves
