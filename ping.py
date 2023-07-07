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

class GameSprite1(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x,player_speed_y, height, weight):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (height,weight))
        self.speed_x=player_speed_x
        self.speed_y=player_speed_y
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

class Ball(GameSprite1):
    def update(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        if self.rect.x>710 or self.rect.x<-10:
            self.kill()

        

player1=Player1('paddle.png', x1,y1,3,30,100)
player2=Player2('paddle.png', x2,y2,3,30,100)
player1.rect.x+=3
ball=Ball('ball.png', 350,250,5,5,40,40)
game=True
finish=False
wait=120
wait1=0
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
        if ball.rect.y>460 or ball.rect.y<=0:
            ball.speed_y*=-1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            if wait1<=0:
                ball.speed_x*=-1
                wait1=15
        if wait1 != 0:
            wait1-=1
    if ball.rect.x>690:
        finish=True
        a=False
        window.blit(win1,(200,200))
        if wait==0:
            wait=120
            finish=False
            a=True
            ball.rect.x=350
            ball.rect.y=250
        else:
            wait-=1
    if ball.rect.x<10:
        finish=True
        window.blit(win2,(200,200))
        a=False 
        if wait==0:
            wait=120
            
            finish=False
            a=True
            ball.rect.x=350
            ball.rect.y=250
        else:
            wait-=1
    display.update()
    clock.tick(FPS)
        
