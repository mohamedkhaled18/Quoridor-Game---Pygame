from constants import *

def is_adjacent(current_position, new_position):
    """ده عشان نمنع حتة الdiagonals يكون فوقو تحت و يمين و شمال بس"""
    curr_row, curr_col = current_position
    new_row, new_col = new_position
    row_diff = abs(new_row - curr_row)
    col_diff = abs(new_col - curr_col)
    
    return row_diff + col_diff == 1

def pixels_to_cells(pixels):
    mx, my = pixels
    row = (my - OFFSET_Y) // SQUARE_SIZE
    col = (mx - OFFSET_X) // SQUARE_SIZE
    
    if 0 <= row < GRID_ROW and 0 <= col < GRID_COL:
        return row, col
    return None

def pixels_to_wall_position(mouse_position, orientation):
    x, y = mouse_position

    # Convert mouse position relative to board
    x -= OFFSET_X
    y -= OFFSET_Y

    # Check if mouse is inside the board
    if x < 0 or y < 0 or x >= BOARD_SIZE or y >= BOARD_SIZE:
        return None

    if orientation == 'h':
        # Find the nearest horizontal boundary
        row = round(y / SQUARE_SIZE) - 1
        col = int(x // SQUARE_SIZE)

        # Check distance from the boundary
        boundary_y = (row + 1) * SQUARE_SIZE
        if abs(y - boundary_y) > WALL_SNAP_DISTANCE:
            return None

    elif orientation == 'v':
        # Find the nearest vertical boundary
        row = int(y // SQUARE_SIZE)
        col = round(x / SQUARE_SIZE) - 1

        # Check distance from the boundary
        boundary_x = (col + 1) * SQUARE_SIZE
        if abs(x - boundary_x) > WALL_SNAP_DISTANCE:
            return None

    else:
        return None

    # Check wall boundaries
    if row < 0 or col < 0:
        return None

    if row >= GRID_ROW - 1 or col >= GRID_COL - 1:
        return None

    return row, col

# center = offset + which square + center in square
def center(position):
    row, col = position
    cx = OFFSET_X + col * SQUARE_SIZE + SQUARE_SIZE // 2
    cy = OFFSET_Y + row * SQUARE_SIZE + SQUARE_SIZE // 2
    return cx, cy