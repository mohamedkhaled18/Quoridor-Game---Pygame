import pygame
from constants import *
from utils_functions import *


class Board:
    
    def __init__(self, window):
        self.h_walls = set()
        self.v_walls = {(0,0)}  
        self.window = window
    
    def total_walls_count(self):
        return len(self.v_walls) + len(self.h_walls)
    
    def add_wall(self, position, orientation):
        if orientation == 'h':
            self.h_walls.add(position)
        elif orientation == 'v':
            self.v_walls.add(position)
            
    def draw_board(self):
        for row in range(GRID_ROW):
            for col in range(GRID_COL):
                rect = pygame.Rect(
                    OFFSET_X + col * SQUARE_SIZE,
                    OFFSET_Y + row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                )
                pygame.draw.rect(self.window, GRID_COLOR, rect, BORDER_WIDTH)

    def draw_player(self, position, color, radius):
        p_center = center(position)
        pygame.draw.circle(self.window, color, p_center, radius)
    
    def draw_wall(self, position, orientation, color=WALL_COLOR):
    
        if orientation.lower() not in ['h', 'v']:
            return

        row, col = position
        x = OFFSET_X + SQUARE_SIZE * col
        y = OFFSET_Y + SQUARE_SIZE * row
        width, height = 0, 0
        
        if orientation.lower() == 'h':
            width = WALL_LENGTH * SQUARE_SIZE
            height = WALL_THICKNESS
            y += SQUARE_SIZE - WALL_THICKNESS // 2
        else:
            width = WALL_THICKNESS
            height = WALL_LENGTH * SQUARE_SIZE
            x += SQUARE_SIZE - WALL_THICKNESS // 2
            
        rect = pygame.Rect(x, y , width, height)
        pygame.draw.rect(self.window, color, rect)
        
    def draw_walls(self):
        for wall in self.v_walls:
            self.draw_wall(wall, 'v')
            
        for wall in self.h_walls:
            self.draw_wall(wall, 'h')
            
    def draw_wall_preview(self, position, orientation, color=LEGAL_WALL_COLOR):
        if position is not None:
            self.draw_wall(position, orientation, color)
            
    def is_wall_legal(self, position, orientation):
        # Check count of walls
        if self.total_walls_count() >= TOTAL_WALLS:
            return False
        
        # Check boundaries
        if position == None or orientation not in ('v', 'h'):
            return False
        
        row, col = position
        is_out_of_bounds = col >= GRID_COL - 1 or row >= GRID_ROW - 1
        if is_out_of_bounds: return False
        
        # Check overlapping = add another wall on a place has already wall
        v_non_allowd_positions = [(row - 1, col), (row, col) ,(row + 1, col)]
        h_non_allowd_positions = [(row, col - 1), (row, col) ,(row, col + 1)]
        
        if orientation == 'h':
            for pos in h_non_allowd_positions:
                if pos in self.h_walls:
                    return False
        elif orientation == 'v':
            for pos in v_non_allowd_positions:
                if pos in self.v_walls:
                    return False
        
        # Check crossing
        if orientation == 'h':
            if position in self.v_walls:
                return False

        elif orientation == 'v':
            if position in self.h_walls:
                return False
            
        # Check paths
        return True