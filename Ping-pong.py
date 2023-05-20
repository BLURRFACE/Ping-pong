from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, p_image, speed, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed


player1 = Player('SS.jpg', 3, 20, 250, 30, 150)
ball = GameSprite('Ball.jpg', 4, 295, 250, 50, 50)
player2 = Player('SS.jpg', 3, 650, 250, 30, 150)

clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption('')
background=transform.scale(image.load('BX.png'), (700, 500))


font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)
lose1 = font1.render('Player1 lose!', True, (255,255,255))
lose2 = font2.render('Player2 Llose!', True, (255,255,0))

speed_x = 3
speed_y = 3
FPS = 120
finish = False
game = True
while game == True:
    for e in event.get():  
        if e.type == QUIT:
            game = False 
    if finish == False:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y <= 0 or ball.rect.y > 450:
            speed_y *=- 1
        window.blit(background, (0,0))
        player1.reset()
        player1.update1()
        player2.reset()
        player2.update2()
        ball.reset()
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *=- 1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (320, 250))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (320, 250))
    display.update()
    clock.tick(FPS)





















