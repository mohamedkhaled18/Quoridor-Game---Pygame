import pygame
from Board import Board
from constants import *
from utils_functions import *


def main():
    pygame.init()
    
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    window.fill(WINDOW_BACKGROUND)
    pygame.display.set_caption("Quoridor")
    board = Board(window)
    
    clock = pygame.time.Clock()

    player1_position = (0, GRID_COL // 2)
    player2_position = (GRID_ROW - 1, GRID_COL // 2)
    
    preview_color = LEGAL_WALL_COLOR
    wall_orientation = 'h'
    is_wall_legal = False

    running = True
    
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    wall_orientation = 'h'
                elif event.key == pygame.K_v:
                    wall_orientation = 'v'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_position = event.pos
                    
                    new_position = pixels_to_cells(mouse_position)
                    wall_position = pixels_to_wall_position(mouse_position, wall_orientation)
                    
                    if is_wall_legal:
                        board.add_wall(wall_position, wall_orientation)
                    
                    elif new_position is not None:
                        if is_adjacent(player1_position, new_position) and new_position != player2_position:
                            player1_position = new_position
        
        mouse_position = pygame.mouse.get_pos()
        wall_position = pixels_to_wall_position(mouse_position, wall_orientation)
        is_wall_legal = board.is_wall_legal(wall_position, wall_orientation)
        
        if is_wall_legal:
            preview_color = LEGAL_WALL_COLOR
        else:
            preview_color = ILLEGAL_WALL_COLOR
            
        window.fill(WINDOW_BACKGROUND)
        board.draw_board()
        board.draw_walls()
        board.draw_wall_preview(wall_position, wall_orientation, preview_color)
        
        board.draw_player(player1_position, PLAYER1_COLOR, PLAYER_RADIUS)
        board.draw_player(player2_position, PLAYER2_COLOR, PLAYER_RADIUS)
        
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()