import pygame as pg



class Bullet(pg.sprite.Sprite):
    def __init__(self, filename, x, y, sc):
        self.screen = screen
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load(filename).convert()
        self.image = pg.transform.scale(img,(2,10))
        self.rect = self.image.get_rect()
        self.y = 10
        self.speedy = 10
        self.rect.y = y
        self.rect.x = x - 5
    def update(self):
        self.rect.y -= self_speedy
    def draw(self):
        self.screen.blit(self.image, self.rect)
