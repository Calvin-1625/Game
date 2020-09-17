import pygame, sys

# initialize Pygame
pygame.init()

# create a canvas 
# pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()
#background surface, image.load("directory").convert()
bg_surface = pygame.image.load('assets/background-day.png').convert()

#Implement the game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# to position the bg-surface blit method in x-axis and y-axis
	screen.blit(bg_surface,(0,0))

	pygame.display.update()
	clock.tick(120) #Frame rate, fps #setting the frame rate


