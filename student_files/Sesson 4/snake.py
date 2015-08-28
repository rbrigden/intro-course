#!/usr/bin/python

# Welcome to the classic game of Snake! Follow the instructions in the lesson
# to complete the code and play the game. Have fun!

# author: Ryan Brigden
# date: 6/11/15

# import modules
import pygame, random, sys
from pygame.locals import *

# determines whether two surfaces are overlapping, aka "collided"
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	''' YOUR CODE GOES HERE '''

# displays score and ends game if player "dies"
def die(screen, score):
	f = pygame.font.SysFont('Arial', 30);
	t = f.render('Your score was: '+str(score), True, (0, 0, 0));
	screen.fill((255, 255, 255))
	screen.blit(t, (10, 270));
	pygame.display.update()
	pygame.time.wait(3000)
	sys.exit(0)

# the snake is represented by an array of x and y positions on which the blocks are placed
# as you can see, the snake is oriented vertically upon start (same x, y descending by 20)
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]

# represents the direction of the snake (modified by the arrow keys)
direction = 0

# score of the game
score = 0

size = height, width = 600, 600
applepos = (random.randint(0, 590), random.randint(0, 590))
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')
appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))

# the blocks that make up the snake
block = pygame.Surface((20, 20))
block.fill((255, 0, 0))

f = pygame.font.SysFont('Arial', 20)

clock = pygame.time.Clock()

# boolean that tells the game to run or stop (True or False)
running = True

while running:
	clock.tick(10) 

	# quit when x clicked and change direction on arrow key press
	for e in pygame.event.get():	
		if e.type == QUIT:
			sys.exit(0)
		elif e.type == KEYDOWN:
			if e.key == K_UP and direction != 0:
				direction = 2
			elif e.key == K_DOWN and direction != 2:
				direction = 0
			elif e.key == K_LEFT and direction != 1:
				direction = 3
			elif e.key == K_RIGHT and direction != 3:
				direction = 1

	# loop through each "block" of the snake and check if it has collided with another block
	# the player "dies" if the snake collides with itself
	i = len(xs)-1
	while i >= 2:
		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
			die(screen, score)
		i-= 1

	# if the snake eats the apple, increment the score
	# and move the apple to a random position
	if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
		score+=1
		xs.append(700)
		ys.append(700)
		applepos=(random.randint(0,590),random.randint(0,590))

	# if the snake moves out of the screen, the player "dies"
	''' YOUR CODE GOES HERE '''

	# move the lead block by the direction of the key press 
	# and have the remaining blocks follow
	i = len(xs)-1
	while i >= 1:
		xs[i] = xs[i-1]
		ys[i] = ys[i-1]
		i -= 1
	if direction==0:
		ys[0] += 20
	elif direction==1:
		xs[0] += 20
	elif direction==2:
		ys[0] -= 20
	elif direction==3:
		xs[0] -= 20
	print xs[0]

	# fill the screen with the background, snake, and apple
	screen.fill((255, 255, 255))
	for i in range(0, len(xs)):
		screen.blit(block, (xs[i], ys[i]))
	screen.blit(appleimage, applepos)
	t = f.render(str(score), True, (0, 0, 0))
	screen.blit(t, (10, 10))
	pygame.display.update()





