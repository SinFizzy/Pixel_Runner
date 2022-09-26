from tkinter import Place
import pygame
from sys import exit


def display_score():
    current_time = pygame.time.pygame.event.get()
    score_surf = test_font.render(f"{current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))  # Origin Point
# Sets the pixel / resolution of the window (width, heigth)
pygame.display.set_caption("Runner")  # Changes the name of the game / display window
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)  # (Font type, Size)
game_active = True

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
# inputing an image into pygame based on location of screen.blit()

# score_surf = test_font.render("My game", False, (64, 64, 64))
# score_rect = score_surf.get_rect(center=(400, 50))
# score_surf(text, Anti Aliesing, color) -- score_rect(turning it into a rect+pos)

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright=(600, 300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0
# Currently this is the only way to place an image at a designated location


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800  # Temp fix for the snail hitting the player after you loss

    # draw all our elements -- if run without player input then player wouldnt be able to close the game
    # update everything -- adding exit on the sys import above always it to end the loop with play action

    # blit stands for "block image transfer" and always you to place one object on another
    # This is the position sky_surface starts the color on the Origin Point
    if game_active:
        screen.blit(sky_surface, (0, 0))  # 0 from the left & 0 from the top
        screen.blit(ground_surface, (0, 300))  # Images overlap based on code position
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)  # Tells pygame you want to draw a rect
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # screen.blit(score_surf, score_rect)

        snail_rect.x -= 4  # Tells the snail to move left with te negitive value
        if snail_rect.right <= 0:
            snail_rect.left = 800
            # Checks to see when the snails has left the screen (800 is the max size of screen)
        screen.blit(snail_surf, snail_rect)  # places the snail at (600, 250) on the screen

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        # player_rect.bottom tells the code to sit the player at that postion which is the ground

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("Yellow")

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]

    # if player_rect.colliderect(snail_rect):
    #    print("collision")

    # mouse_pos = pygame.mouse.get_pos()  # Tells pygame to take mouse position into account
    # if player_rect.collidepoint(mouse_pos):  # If mouse collides with player then prints
    #    print(pygame.mouse.get_pressed()) #Takes Left click, Middle mouse button & Right click into acct while print True or False

    pygame.display.update()
    clock.tick(60)  # This True loop wont run faster than 60 fps (Max Frame Rate)
