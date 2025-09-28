from pygame import *

win = display.set_mode((700,500))
display.set_caption('Пинг-понг')
win.fill((0,100,255))
clock = time.Clock()
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, hight):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, hight))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y <= 350:
            self.rect.y += self.speed

    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= 350:
            self.rect.y += self.speed

player1 = Player('racket.png', 0, 250, 3, 50, 150)
player2 = Player('racket.png', 650, 250, 3, 50, 150)


finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        win.fill((0,100,255))
        player1.update1()
        player1.reset()
        player2.update2()
        player2.reset()

        #if sprite.collide



    clock.tick(60)
    display.update()