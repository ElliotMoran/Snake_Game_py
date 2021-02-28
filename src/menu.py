import sys
import pygame
import settings


class Button:
    def __init__(self, x_pos: int, y_pos: int, x_size: int, y_size: int, text=""):
        pygame.font.init()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_size = x_size
        self.y_size = y_size

        self.normal_color = settings.DARK_GRAY
        self.sellected_color = settings.LIGHT_GRAY
        self.color = self.normal_color

        self.text = text
        self.font = pygame.font.SysFont('Arial', 25, bold=True)
        self.text_color = settings.BLACK

    def on_click(self) -> None:
        pass

    def check_state(self) -> None:
        mouse = pygame.mouse
        if mouse.get_focused():
            mouse_x, mouse_y = mouse.get_pos()
            if mouse_x >= self.x_pos and mouse_x <= self.x_pos + self.x_size:
                if mouse_y >= self.y_pos and mouse_y <= self.y_pos + self.y_size:
                    if mouse.get_pressed()[0]:
                        # if button was pressed
                        self.color = self.sellected_color
                        self.on_click()
                    else:
                        # if mouse on button
                        self.color = self.sellected_color
            else:
                # normal button state
                self.color = self.normal_color

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.rect(screen, self.color,
                         (self.x_pos, self.y_pos, self.x_size, self.y_size))

        render = self.font.render(self.text, 0, self.text_color)
        screen.blit(render, (self.x_pos + self.x_size // 2 - 5,
                             self.y_pos + self.y_size // 2 - 5))


class Start_game_button(Button):
    def __init__(self, x_pos: int, y_pos: int, x_size: int, y_size: int):
        super().__init__(x_pos, y_pos, x_size, y_size, "START")

    def on_click(self) -> None:
        print("START")


class Exit_button(Button):
    def __init__(self, x_pos: int, y_pos: int, x_size: int, y_size: int):
        super().__init__(x_pos, y_pos, x_size, y_size, "EXIT")

    def on_click(self) -> None:
        print("EXIT")
        sys.exit()


class Menu:
    def __init__(self):
        self.start_button = Start_game_button(500, 250, 100, 50)
        self.exit_button = Exit_button(500, 350, 100, 50)

        self.buttons = [self.start_button, self.exit_button]

    def main_loop(self, screen: pygame.display) -> None:
        screen.fill(settings.WHITE)
        in_menu = True
        while in_menu:
            for button in self.buttons:
                button.draw(screen)
                button.check_state()
