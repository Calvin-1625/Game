import pygame, sys

# dedicate for mounting the base surface on the image
def draw_base():
	screen.blit(base_surface,(base_x_pos, 450))
	screen.blit(base_surface,(base_x_pos + 288, 450))



# initialize Pygame
pygame.init()

# create a canvas 
# pygame.display.set_mode((width, height))
screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

# initialize the gravity we will use
gravity = 0.25
bird_movement = 0

#background surface, image.load("directory").convert()
bg_surface = pygame.image.load('assets/background-day.png').convert()
# scale image to screen dimnesion
##bg_surface = pygame.transform.scale2x(bg_surface)
# base image
base_surface = pygame.image.load('assets/base.png').convert()
base_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50, 256))

#Implement the game loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_movement = 0
				bird_movement -= 6
				print("Space Bar")
	# to position the bg-surface blit method in x-axis and y-axis top left  
	screen.blit(bg_surface,(0,0))
	bird_movement += gravity
	#center x left and right center y up and down
	bird_rect.centery += bird_movement
	screen.blit(bird_surface, bird_rect)
	base_x_pos -=1 # animation effect for the base x axis(+ move to right , - move to left)
	draw_base()
	if base_x_pos <= -288 :
		base_x_pos = 0

	pygame.display.update()
	clock.tick(120) #Frame rate, fps #setting the frame rate


