import pygame
import sys
from settings import Settings
from ship import Ship

from pygame.sprite import Group
import gameFunctions as gf
def runGame():
    pygame.init()
    aiSettings = Settings()
    screen = pygame.display.set_mode((aiSettings.screenWidth,aiSettings.screenHeight))
    pygame.display.set_caption("Alien Invision")
    ship = Ship(aiSettings,screen)
    bullets = Group()
    while True:
        # gf.checkEvents(ship)
        gf.checkEvents(aiSettings,screen,ship,bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateScreen(aiSettings,screen,ship,bullets)
runGame()