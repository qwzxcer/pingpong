from random import *
from pygame import *
win_height = 700
win_width = 500
x1=20
y1=200
x2=650
y2=350
window=display.set_mode((700,500))
clock = time.Clock()
FPS=60
display.set_caption("ping pong")
background=transform.scale(image.load("bluescene.png"),(win_height,win_width))
window.blit(background,(0,0))
font.init()
font = font.Font(None, 70)
win1 = font.render('player1 win!', True, (255,0,0))
win2 = font.render('player2 win!', True, (255,0,0))
a=True
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
            global a
            if a:
                keys_pressed=key.get_pressed()
                if keys_pressed[K_w] and self.rect.y >5:
                    self.rect.y -=self.speed
                if keys_pressed[K_s] and self.rect.y <395:
                    self.rect.y +=self.speed

class Player2(GameSprite):
    def update(self):
        global a
        if a:
                keys_pressed=key.get_pressed()
                if keys_pressed[K_UP] and self.rect.y >5:
                    self.rect.y -=self.speed
                if keys_pressed[K_DOWN] and self.rect.y <395:
                    self.rect.y +=self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x+=self.speed
        if self.rect.x>800 or self.rect.x<-100 or self.rect.y>600 or self.rect.y<-100:
            self.kill()

        

player1=Player1('paddle.png', x1,y1,3,30,100)
player2=Player2('paddle.png', x2,y2,3,30,100)
ball=Ball('ball.png', 350,250,5,40,40)
game=True
finish=False
wait=120
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
    if finish == False:
        if sprite.collide_rect(ball, player2):
            ball.rect.x -=ball.speed
        if sprite.collide_rect(ball, player1):
            ball.rect.x +=ball.speed
    if ball.rect.x>690:
        finish=True
        a=False
        window.blit(win1,(200,200))
        if wait==0:
            wait==120
            finish=False
            a=True
        else:
            wait-=1
    if ball.rect.x<10:
        finish=True
        window.blit(win2,(200,200))
        a=False 
        if wait==0:
            wait==120
            finish=False
            a=True
        else:
            wait-=1  
    display.update()
    clock.tick(FPS)
        
