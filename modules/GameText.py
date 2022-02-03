text_obj = {
    "menu": [],
    "game": []
}


class GameText:
    def __init__(self, transform: tuple, font, text: str, color_rgb: tuple, tag: str):
        self.transform = transform
        self.font = font
        self.text = text
        self.color_rgb = color_rgb
        self.sprite = self.font.render(self.text, True, self.color_rgb)

        text_obj[tag].append(self)

    def render(self, screen):
        # Getting the center of the text
        sprite_transform = (
            self.transform[0] - (self.sprite.get_width() / 2),
            self.transform[1] - (self.sprite.get_height() / 2)
        )

        # Rendering the text image
        screen.blit(self.sprite, sprite_transform)

    def change_text(self, new_text):
        self.text = str(new_text)
        self.sprite = self.font.render(self.text, True, self.color_rgb)
