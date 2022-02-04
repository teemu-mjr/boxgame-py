from modules.GameText import GameText


class ScoreText(GameText):
    def __init__(self, transform: tuple, font, text: str, color_rgb: tuple):
        super().__init__(transform, font, text, color_rgb)
        self.score = 0

    def add_score(self, value):
        self.score += value
        self.change_text(self.score)
