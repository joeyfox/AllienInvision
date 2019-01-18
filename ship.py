import pygame
class Ship():
    def __init__(self,settings,screen):
        self.screen = screen
        self.aiSettings = settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()

        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom

        self.center = float(self.rect.centerx)

        self.movingRight = False
        self.movingLeft = False
        self.movingTop = False
        self.movingBottom = False
    def update(self):
        if self.movingRight and self.rect.right < self.screenRect.right:
            self.center += self.aiSettings.shipSpeedFactor
        elif self.movingLeft and self.rect.left >0:
            self.center -= self.aiSettings.shipSpeedFactor
        elif self.movingTop:
            self.rect.bottom -= self.aiSettings.shipSpeedFactor
            # self.rect.top += self.aiSettings.shipSpeedFactor
        elif self.movingBottom:
            self.rect.bottom += self.aiSettings.shipSpeedFactor
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image,self.rect)