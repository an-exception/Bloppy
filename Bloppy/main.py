import pygame as pg
import random
from tkinter import messagebox

pg.init()


display = pg.display.set_mode([600, 600])
pg.display.set_caption('Bloppy')


running = True
started = False
points = 0
clock = pg.time.Clock()
ball_pos = pg.Vector2(300, 300)
ball_velo = 0
pipe_pos = pg.Vector2(650, random.randint(50, 550))

font = pg.font.SysFont('Consolas', 50)

def reset():
    global started, ball_pos, ball_velo, pipe_pos, points
    started = False
    ball_pos = pg.Vector2(300, 300)
    ball_velo = 0
    pipe_pos = pg.Vector2(650, random.randint(50, 550))

    messagebox.showinfo('Should Have Done Better', f'POINTS: {points} \nScreenshot this for record.')
    points = 0

while running:
    if pg.event.get(pg.QUIT):
        running = False

    display.fill('skyblue')
    pipe = pg.draw.rect(display, 'green', pg.Rect(pipe_pos.x, pipe_pos.y, 50, 550))
    pipe2 = pg.draw.rect(display, 'green', pg.Rect(pipe_pos.x, pipe_pos.y - 700, 50, 550))
    ball = pg.draw.circle(display, 'red', ball_pos, 20)

    pts = font.render(str(points), True, 'black')
    display.blit(pts, [(600 / 2 - (12.5 * len(str(points)))), 10])

    if ((ball_pos.x + 20) > pipe_pos.x and (ball_pos.y + 20) > pipe.y and not (ball_pos.x - 20) > pipe_pos.x + 50) or ((ball_pos.x + 20) > pipe_pos.x and (ball_pos.y - 20) < (pipe.y - 150) and not (ball_pos.x + 20) > pipe_pos.x + 50):
        reset()
      
    if started: 
        for key in pg.event.get(pg.KEYDOWN): 
            if ball_pos.y < 0: ball_pos.y = 20

            if key.key == pg.K_SPACE:
                ball_velo = -13

        else:
            if ball_pos.y > 580: reset()

            ball_velo += 1
            ball_pos.y += ball_velo
        
        if pipe_pos.x > -40:
            pipe_pos.x -= 5

        else:
            pipe_pos.x = 650
            pipe_pos.y = random.randint(50, 550)
            points += 1

    else:
        for key in pg.event.get(pg.KEYDOWN):
            if key.key == pg.K_SPACE:
                started = True
                ball_velo = -13

    pg.display.update()
    clock.tick(60)


pg.quit()
