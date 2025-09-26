import pygame as pg
from player import player 



clock = pg.time.Clock()
running = True
pill = player()

#mainloop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and (pill.x_loc >=0):
        pill.move_left()
    
    if keys[pg.K_RIGHT] and (pill.x_loc <= 520):
         pill.move_right()

    # flip() the display to put your work on screen

    pill.bg_update()
    clock.tick(60)  # limits FPS to 60

pg.quit()