from pygame import *

clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption('')
background=transform.scale(image.load('Background.jpg'), (700, 500))

FPS = 120
finish = False
game = True
while game == True:
    for e in event.get():  
        if e.type == QUIT:
            game = False 
    if finish == False:
        window.blit(background, (0,0))
    display.update()
    clock.tick(FPS)





















