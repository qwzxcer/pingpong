from random import *
from pygame import *
win_height = 700
win_width = 500
x1=20
y1=200
x2=670
y2=350
window=display.set_mode((700,500))
clock = time.Clock()
FPS=60
display.set_caption("ping pong")
background=transform.scale(image.load("bluescene.png"),(win_height,win_width))
window.blit(background,(0,0))
font.init()
fontl=font.Font(None, 36)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, weight):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (height,weight))
        self.speed=player_speed
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
            keys_pressed=key.get_pressed()
            if keys_pressed[K_w] and self.rect.y >5:
                self.rect.y -=self.speed
            if keys_pressed[K_s] and self.rect.y <395:
                self.rect.y +=self.speed

class Player2(GameSprite):
    def update(self):
            keys_pressed=key.get_pressed()
            if keys_pressed[K_UP] and self.rect.y >5:
                self.rect.y -=self.speed
            if keys_pressed[K_DOWN] and self.rect.y <395:
                self.rect.y +=self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed

player1=Player1('paddle.png', x1,y1,3,30,100)
player2=Player2('paddle.png', x2,y2,3,30,100)
ball=Ball('ball.png', 350,250,3,30,30)
game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    window.blit(background,(0,0))
    player1.reset()
    player2.reset()
    player1.update()
    player2.update()
    ball.reset()
    ball.update()

    display.update()
    clock.tick(FPS)

        