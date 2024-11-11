import pygame

import runner
from runner import main

pygame.init()
grey = (128,128,128)

clock = pygame.time.Clock()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
    )
screen.fill((135, 206, 235))
Titlefont = pygame.font.Font('freesansbold.ttf', 32)
font = pygame.font.Font('freesansbold.ttf',11)
text = Titlefont.render('Flappy Bird Game', True, (0,0,0))
textRect = text.get_rect()
textRect.center = (960, 400)
start_button = pygame.Surface((100,50))
startRect = start_button.get_rect(center =(960,540))
startText = font.render('Click here to Start', True, (255, 255, 255))
buttonText = startText.get_rect(center = (960,540))
screen.blit(text,textRect)




running = True
while running:
   mx, my = pygame.mouse.get_pos()
   mousesurf = pygame.Surface((1, 1))
   mousesurf.fill((255,255,255))
   mouserect = mousesurf.get_rect(center=(mx, my))

   if mouserect.colliderect(startRect):
       start_button.fill(grey)
   else:
       start_button.fill((0, 0, 0))
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
       if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings = False
                    playing = True

       if event.type == pygame.MOUSEBUTTONDOWN:
           if mouserect.colliderect(startRect):
                runner.main()

   screen.blit(mousesurf, mouserect)
   screen.blit(start_button, startRect)
   screen.blit(startText, buttonText)
   pygame.display.flip()

   clock.tick(120)