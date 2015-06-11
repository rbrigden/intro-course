# import modules
import pygame, random, sys
from pygame.locals import *

def main():
    
    # initialize the pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("./python_games/Star.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("blank game")

    # size of surface on screen
    size = height, width = 900, 900
    
    # create a surface on screen
    screen = pygame.display.set_mode(size)
    
    # define a variable to control the main loop
    running = True

    # setup the clock
    clock = pygame.time.Clock()

    # initial position of the star
    x = 200
    y = 200

    # initial speed of the star
    xspeed = 15
    yspeed = 10

    # difference in time for motion
    # to increase smooth flow
    dt = 0.001

    # c1 = pygame.draw.circle(screen, (255, 0, 0), (40,40), 30)
    # img = pygame.Surface((20, 20))
    bg = pygame.Surface(size)
    bg.fill((255,0,0))

    
    # main loop
    while running:
        clock.tick(30)
        screen.blit(bg, (0,0))

        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    xspeed += 5
                if event.key == K_LEFT:
                    xspeed -= 5
        
        if x > width or x < 0:
            xspeed *= -1
        if y > height-100 or y < 0:
            yspeed *= -1

        for i in range(1,1000): 
            # screen.blit(img, (10,10))
            x += xspeed * dt
            y += yspeed * dt
            screen.blit(logo, (x, y))


        pygame.display.flip()


    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
