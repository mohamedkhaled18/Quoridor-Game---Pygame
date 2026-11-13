import pygame

from constants import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_BACKGROUND,
    GRID_ROW, GRID_COL, SQUARE_SIZE, GRID_COLOR, BORDER_WIDTH,
    OFFSET_X, OFFSET_Y,
    PLAYER1_COLOR, PLAYER2_COLOR, PLAYER_RADIUS,
)
from utils_functions import center, pixels_to_cells, is_adjacent, get_legal_moves


def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Quoridor")
    clock = pygame.time.Clock()

    player1_position = (0, GRID_COL // 2)
    player2_position = (GRID_ROW - 1, GRID_COL // 2)

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_position = pixels_to_cells(event.pos)
                    if new_position is not None:
                        if is_adjacent(player1_position, new_position) and new_position != player2_position:
                            player1_position = new_position

        window.fill(WINDOW_BACKGROUND)

        for row in range(GRID_ROW):
            for col in range(GRID_COL):
                rect = pygame.Rect(
                    OFFSET_X + col * SQUARE_SIZE,
                    OFFSET_Y + row * SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                )
                pygame.draw.rect(window, GRID_COLOR, rect, BORDER_WIDTH)

        p2_center = center(player2_position)
        p1_center = center(player1_position)

        pygame.draw.circle(window, PLAYER1_COLOR, p1_center, PLAYER_RADIUS)
        pygame.draw.circle(window, PLAYER2_COLOR, p2_center, PLAYER_RADIUS)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()