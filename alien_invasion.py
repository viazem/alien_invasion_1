import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Инициализирует pygame, settings и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Создаем корабль
    ship = Ship(ai_settings, screen)
    # Создаем группы для хранения пуль.
    bullets = Group()

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # При каждом проходе цикла перерисовывается экран.
        # Отображение последнего прорисованного экрана
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
