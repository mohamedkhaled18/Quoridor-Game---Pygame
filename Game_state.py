# game_state.py
from constants import GRID_ROW, GRID_COL


class GameState:
    def __init__(self):
        self.player1_pos = (0 , GRID_COL // 2)
        self.player2_pos = (GRID_ROW - 1 , GRID_COL // 2)
        self.h_walls = set()                  # حوائط أفقية
        self.v_walls = set()                  # حوائط رأسية
        self.current_turn = 1                 # 1 أو 2
        self.walls_left = {1: 10, 2: 10}      # كل لاعب عنده 10 حوائط

    def get_legal_moves(self, player):
        """ترجع قائمة الخانات اللي اللاعب يقدر يتحرك لها."""
        ...

    def is_wall_valid(self, orientation, row, col):
        """هل الحائط ده قانوني؟ (مش متقاطع، ومش بيقفل الطريق)"""
        ...

    def place_wall(self, orientation, row, col):
        """تحط حائط وتقلل العداد."""
        ...

    def has_won(self, player):
        """هل اللاعب وصل للصف اللي عايزه؟"""
        ...

    def clone(self):
        """نسخة جديدة من الحالة (للـ AI)."""
        ...