from pygame import *

class Button(sprite.Sprite):
    def __init__ (self, x, y, w, h, color, text, win):
        self.image = Rect(x, y, w, h)
        self.img = Surface((w, h))
        self.rect = self.img.get_rect()
        self.text = font.SysFont('arial', 24).render(text, True, (0,0,0))
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.win = win
    def fill_rect(self):
        draw.rect(self.win, self.color, self.image)
    def outline(self, size): #обводка существующего прямоугольника
        draw.rect(self.win, (0,0,0), self.image, size)
    def txt_render(self):
        self.win.blit(self.text, (self.rect.x + 50, self.rect.y + 15))
    def collidepoint(self, x, y):
        return self.image.collidepoint(x, y)

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed_x, speed_y, win, angel):
        self.img = transform.rotate(transform.scale(image.load(img), (w, h)), angel)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.win = win
    def draw(self):
        self.win.blit(self.img, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def move(self):
        self.rect.y += self.speed_y

class Ball(GameSprite):
    def move(self, racket1, racket2):
        self.rect.x += self.speed_x * 1.5
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 440:
            self.speed_y *= -1
        if self.rect.colliderect(racket1) or self.rect.colliderect(racket2):
            self.speed_x *= -1
            if self.speed_x < 0:
                self.speed_x -= 1
            elif self.speed_x > 0:
                self.speed_x -= 1
            if self.speed_y < 0:
                self.speed_y -= 1
            elif self.speed_y > 0:
                self.speed_y -= 1