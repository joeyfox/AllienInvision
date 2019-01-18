import sys
import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
def checkEvents(aiSettings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event,aiSettings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event,ship)

def checkKeyDownEvents(event,aiSettings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_DOWN:
        ship.movingBottom = True
    elif event.key == pygame.K_UP:
        ship.movingTop = True
    elif event.key == pygame.K_SPACE:
        fireBullet(aiSettings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fireBullet(aiSettings,screen,ship,bullets):
    if len(bullets) < aiSettings.bulletAllowed:
        newBullet = Bullet(aiSettings, screen, ship)
        bullets.add(newBullet)
def checkKeyUpEvents(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
    elif event.key == pygame.K_DOWN:
        ship.movingBottom = False
    elif event.key == pygame.K_UP:
        ship.movingTop = False
def updateScreen(aisettings,screen,ship,bullets):
    screen.fill(aisettings.bgColor)
    for bullet in bullets:
        bullet.drawBullet()
    ship.blitme()
    pygame.display.flip()
def updateBullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 :
            bullets.remove(bullet)

