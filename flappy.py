import pygame, sys

# dedicate for mounting the base surface on the image
def draw_base():
	screen.blit(base_surface,(base_x_pos, 450))
	screen.blit(base_surface,(base_x_pos + 288, 450))

def create_pipe():
	new_pipe = pipe_surface.get_rect(midtop = (350, 256))
	return new_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 2.5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		screen.blit(pipe_surface, pipe)


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

pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_list = []
#USEREVENT  is triggered by timer
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)


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
				#print("Space Bar")
		if event.type == SPAWNPIPE:
			pipe_list.append(create_pipe())
			print(pipe_list)
	# to position the bg-surface blit method in x-axis and y-axis top left  
	screen.blit(bg_surface,(0,0))
	
	bird_movement += gravity
	#center x left and right center y up and down
	bird_rect.centery += bird_movement
	screen.blit(bird_surface, bird_rect)

	pipe_list = move_pipes(pipe_list)
	draw_pipes(pipe_list)
	
	base_x_pos -=1 # animation effect for the base x axis(+ move to right , - move to left)
	draw_base()
	if base_x_pos <= -288 :
		base_x_pos = 0

	pygame.display.update()
	clock.tick(120) #Frame rate, fps #setting the frame rate


