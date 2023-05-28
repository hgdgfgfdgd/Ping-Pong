from classies import Racket, Ball, Button
from pygame import * 
font.init()
mixer.init()
from random import randint

bx = randint(1,2)
if bx == 1:
    bx = -3
else:
    bx = 3

by = randint(1,2)
if by == 1:
    by = -3
else:
    by = 3

#переменные
run = True
clock = time.Clock()
mode = 'menu'
win_width = 1000
win_height = 500
counter = 0
x, y = 0, 0

main_win = display.set_mode((1000, 500))
display.set_caption("ping-pong")
bg = transform.scale(image.load('img2.jpg'), (win_width, win_height))
racket1 = Racket('racket1.jpg', 50, 100, 120, 20, 0, 0, main_win, 270)
racket2 = Racket('racket2.jpg', 930, 100, 120, 20, 0, 0, main_win, 90)
ball = Ball('ball5.png', 500, 220, 70, 40, bx, by, main_win, 1)

btn_start = Button(
    win_width/2 - win_width/10, 
    win_height/2 - win_height/10,
    win_width/5,
    win_height/10,  
    (255, 255, 0), 
    'START',
    main_win)
btn_exit = Button(
    win_width/2 - win_width/10, 
    win_height/2 + win_height/10,
    win_width/5,
    win_height/10, 
    (255, 255, 0), 
    '  EXIT',
    main_win)

#mixer.music.load('video.ogg.ogg')
#mixer.music.play()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_UP:
                racket2.speed_y = -7
            if e.key == K_DOWN:
                racket2.speed_y = 7
            
            if e.key == K_w:
                racket1.speed_y = -7
            if e.key == K_s:
                racket1.speed_y = 7

        if e.type == KEYUP:

            if e.key == K_UP:
                racket2.speed_y = 0
            if e.key == K_DOWN:
                racket2.speed_y = 0

            if e.key == K_w:
                racket1.speed_y = 0
            if e.key == K_s:
                racket1.speed_y = 0
        if e.type == MOUSEBUTTONDOWN:
            x, y = e.pos


    if btn_start.collidepoint(x,y) and mode == 'menu':
        mode = 'game'
        x, y = 0, 0
        racket1 = Racket('racket1.jpg', 50, 100, 120, 20, 0, 0, main_win, 270)
        racket2 = Racket('racket2.jpg', 930, 100, 120, 20, 0, 0, main_win, 90)
        ball = Ball('ball5.png', 500, 220, 70, 40, bx, by, main_win, 1)
        
    if btn_exit.collidepoint(x,y) and mode == 'menu':
        run = False

    main_win.blit(bg, (0, 0))
    if mode == 'game':
        racket1.move()
        racket2.move()
        racket1.draw()
        racket2.draw()
        ball.draw()
        ball.move(racket1, racket2)

        if ball.rect.x > 910:
            res_label = font.SysFont('Courier New', 52, 1).render('Левая ракетка победитель!', True, (0,0,0))
            mode = 'res'
        if ball.rect.x < 30:
            res_label = font.SysFont('Courier New', 52, 1).render('Правая ракетка победитель!', True, (0,0,0))
            mode = 'res'

    if mode == 'res':
        main_win.blit(res_label, (150, 200))
        counter += 1
        if counter > 180:
            counter = 0
            mode = 'menu'

    if mode == 'menu':
        btn_start.fill_rect()
        btn_start.outline(3)
        btn_start.txt_render()
        btn_exit.fill_rect()
        btn_exit.outline(3)
        btn_exit.txt_render()

    display.update()
    clock.tick(60)