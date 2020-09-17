import pygame, sys, random

# dedicate for mounting the base surface on the image
def draw_base():
	screen.blit(base_surface,(base_x_pos, 450))
	screen.blit(base_surface,(base_x_pos + 288, 450))

def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (350, random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom = (350, random_pipe_pos - 150 ))
	return bottom_pipe, top_pipe

def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 2.5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.bottom >= 512:
			screen.blit(pipe_surface, pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface, False, True) # False for the x axis, True for the y axis
			screen.blit(flip_pipe, pipe)

def check_collision(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			print("collision detected")
	if bird_rect.top <= -50 or bird_rect.bottom >= 450:
		print("collision detected")
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
pipe_height = [200, 300, 400]


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
			pipe_list.extend(create_pipe())
			# print(pipe_list)
	# to position the bg-surface blit method in x-axis and y-axis top left  
	screen.blit(bg_surface,(0,0))
	
	bird_movement += gravity
	#center x left and right center y up and down
	bird_rect.centery += bird_movement
	screen.blit(bird_surface, bird_rect)
	check_collision(pipe_list)

	pipe_list = move_pipes(pipe_list)
	draw_pipes(pipe_list)
	
	base_x_pos -=1 # animation effect for the base x axis(+ move to right , - move to left)
	draw_base()
	if base_x_pos <= -288 :
		base_x_pos = 0

	pygame.display.update()
	clock.tick(120) #Frame rate, fps #setting the frame rate


