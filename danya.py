import pygame
import os

directory = os.path.dirname(__file__)

pygame.init()

textures_img_links = os.path.abspath(directory + "/textures")

floor_black = pygame.image.load(textures_img_links + "/black.png")
wall_gras = pygame.image.load(textures_img_links + "/grass.png")
character = pygame.image.load(textures_img_links + "/creeper.png")
character = pygame.transform.scale(character, (20, 25))
freddy_image = pygame.image.load(textures_img_links + "/freddy.png")

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800))

player = pygame.Rect(15, 15, 20, 25)
freddy = pygame.Rect(770, 770, 17, 27)

go_D = False 
go_A = False
go_W = False
go_S = False

game = True

textures = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
]
    
rects = []
rects_textures = []

bad_rects = []

x = 0
y = 0

for texture_draw in textures:
    for i in texture_draw:
        cube = pygame.Rect(x,y,50,50)
        rects.append(cube)
        rects_textures.append(i)
        if i == 1:
            bad_rects.append(cube)
        x += 50
    y += 50
    x = 0

run = True

textures_amount = len(rects_textures)

font = pygame.font.SysFont("Colibri", 50)
text = font.render("BOOM, EAZY WIN", True, (254,0,0))

while run:
    screen.fill((55, 165, 225))

    for i in range(textures_amount):
        if rects_textures[i] == 0:
            screen.blit(floor_black, rects[i])
        if rects_textures[i] == 1:
            screen.blit(wall_gras, rects[i]) 

    screen.blit(character, player) 
    screen.blit(freddy_image, freddy)

    for i in bad_rects:
        if player.colliderect(i):
            player.x = 15
            player.y = 15

    if player.colliderect(freddy): 
        screen.fill((0, 0, 0))
        screen.blit(text, (300, 400))
        
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                run = False

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_d or i.key == pygame.K_RIGHT:   
                go_D = True    
            if i.key == pygame.K_a or i.key == pygame.K_LEFT:                                         
                go_A = True
            if i.key == pygame.K_s or i.key == pygame.K_DOWN:
                go_S = True
            if i.key == pygame.K_w or i.key == pygame.K_UP:
                go_W = True

        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_d or i.key == pygame.K_RIGHT:
                go_D = False
            if i.key == pygame.K_a or i.key == pygame.K_LEFT:
                go_A = False
            if i.key == pygame.K_s or i.key == pygame.K_DOWN:
                go_S = False
            if i.key == pygame.K_w or i.key == pygame.K_UP:
                go_W = False     

    if  go_D == True :
        player.x += 10
    if  go_A == True :
        player.x -= 10
    if  go_W == True :
        player.y -= 10 
    if  go_S == True :
        player.y += 10   

    pygame.display.flip()
    clock.tick(60)