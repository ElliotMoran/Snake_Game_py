import pygame
import settings


class Button:
    def __init__(self, x: int, y: int, x_size: int, y_size: int, text: str = "") -> None:
        self.x = x
        self.y = y
        self.x_size = x_size
        self.y_size = y_size
        self.text = text

        self.color_default = settings.DARK_GRAY
        self.color_selected = settings.LIGHT_GRAY
        self.color = self.color_default

        self.font = pygame.font.Font('data/fonts/menu_font.ttf', 30)
        self.font_color = settings.BLACK

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.x_size, self.y_size))

        text_render = self.font.render(self.text, 2, self.font_color)
        screen.blit(text_render, (self.x + 30, self.y + 10))

    def check_state(self) -> None:
        mouse=pygame.mouse
        mouse_x, mouse_y=mouse.get_pos()

        if mouse_x >= self.x and mouse_x <= self.x + self.x_size:
            if mouse_y >= self.y and mouse_y <= self.y + self.y_size:
                self.color=self.color_selected
                if mouse.get_focused():
                    if mouse.get_pressed()[0]:
                        self.on_click()
            else:
                self.color=self.color_default
        else:
            self.color=self.color_default

    def on_click(self):
        print(f"{self.text} button was pressed!")


class Menu:
    def __init__(self) -> None:
        self.start_button=Button(250, 50, 150, 50, "START")
        self.exit_button=Button(250, 150, 150, 50, "EXIT")

        self.buttons=[self.start_button, self.exit_button]

    def update(self, screen: pygame.display) -> None:
        for button in self.buttons:
            button.check_state()
            button.draw(screen)
