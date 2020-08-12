import pygame
screen = pygame.display.set_mode((600,600))
white = (255,255,255)
pygame.init()
red = (255,0,50)
black = (0,0,0)
field = pygame.image.load("1jpg.jpg")
background = field.get_rect(bottomright=(1900,1000))

screen.fill(white)
screen.blit(field, background)
while True:   
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.circle(screen, red, i.pos, 5)
                pygame.display.update()
            if i.button == 3:
                pygame.draw.circle(screen, black, i.pos, 10)
                pygame.display.update()
    pygame.time.delay(50)
    

