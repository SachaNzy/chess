import pygame   
from pygame import mixer
pygame.init()
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
color = (255, 255, 255)
font = pygame.font.SysFont("arial", 30)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Menu Space Invaders')
fond = pygame.image.load('assets/background.jpg')

#load button images
menu = True
while menu:

	screen.blit(fond,(0,0))
	text = font.render("C'EST parti !! APPUYEZ SUR LA BARRE D'ESPACE  ", True, color)
	screen.blit(text, (320, 300))
                	
	for event in pygame.event.get():
		# quitter le menu 
				

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				menu = False
				

	pygame.display.update()		
pygame.quit()
