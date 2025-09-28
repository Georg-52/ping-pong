from pygame import *

win = display.set_mode((700,500))
display.set_caption('Пинг-понг')
win.fill((0,100,255))
clock = time.Clock()
game = True
speed_x = 3
speed_y =3
font.init()
font1 = font.SysFont('Arial', 36)

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

player1 = Player('racket.png', 0, 150, 3, 50, 150)
player2 = Player('racket.png', 650, 150, 3, 50, 150)
ball = GameSprite('tenis_ball.png', 350, 250, 3 , 50, 50)


finish = False
text_lose1 = font1.render('ИГРОК 1 ПРОИГРАЛ', True, (255,255,255))
text_lose2 = font1.render('ИГРОК 2 ПРОИГРАЛ', True, (255,255,255))


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
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > 650:
            win.blit(text_lose2, (200, 200))
            finish = True
        if ball.rect.x < 0:
            win.blit(text_lose1, (200, 200))
            finish = True

        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            speed_x *= -1

    else:
        finish = False
        speed_x = 3
        speed_y = 3
        player1.kill()
        player2.kill()
        ball.kill()
        time.delay(3000)
        player1 = Player('racket.png', 0, 250, 3, 50, 150)
        player2 = Player('racket.png', 650, 250, 3, 50, 150)
        ball = GameSprite('tenis_ball.png', 350, 250, 3 , 50, 50)
        


    clock.tick(60)
    display.update()