import pygame 
import pygame.freetype

from Levels_gameplay import Levels_gameplay


def Menu_inicial(screen):
     my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
     i = 0
     y = 350
     l1 = 3
     l2 = 4 
     level = 0
     teste1 = Levels_gameplay(screen, level)
     # Desenha no ecrã os botoẽs das opções 
     while i < 6:
         pygame.draw.rect(screen, (150,0,0), (490, y, 300, 50), 0)
         my_font.render_to(screen, (610, y + 15), str(l1) + " X " + str(l2), (0,0,0))
         y += 60
         i += 1
         if i < 4:
             l1 += 1
         if i > 3:
             l2 += 1
    
     pygame.draw.rect(screen, (150,0,0), (50, 720, 300, 50), 6)
     my_font.render_to(screen, (175, 735), "EXIT", (255,0,0))

     x_m = pygame.mouse.get_pos()[0]
     y_m = pygame.mouse.get_pos()[1]

     mb = pygame.mouse.get_pressed()
     if 490 < x_m < 790 and 350 < y_m < 400:
         pygame.draw.rect(screen, (255,0,0), (490, 350, 300, 50), 6)
         if mb[0] == True:
             level = 1
             teste1.game(screen, level)
             main()

     elif 490 < x_m < 790 and 410 < y_m < 460:
         pygame.draw.rect(screen, (255,0,0), (490, 410, 300, 50), 6)
         if mb[0] == True:
             level = 2
             teste1.game(screen, level)
             main()
    
     elif 490 < x_m < 790 and 470 < y_m < 520:
         pygame.draw.rect(screen, (255,0,0), (490, 470, 300, 50), 6)
         if mb[0] == True:
             level = 3
             teste1.game(screen, level)
             main()

     elif 490 < x_m < 790 and 530 < y_m < 580:
         pygame.draw.rect(screen, (255,0,0), (490, 530, 300, 50), 6)
         if mb[0] == True:
             level = 4
             teste1.game(screen, level)
             main()
    
     elif 490 < x_m < 790 and 590 < y_m < 640:
         pygame.draw.rect(screen, (255,0,0), (490, 590, 300, 50), 6)
         if mb[0] == True:
             level = 5
             teste1.game(screen, level)
             main()
    
     elif 490 < x_m < 790 and 650 < y_m < 700:
         pygame.draw.rect(screen, (255,0,0), (490, 650, 300, 50), 6)
         if mb[0] == True:
             level = 6
             teste1.game(screen, level)
             main()
    
     elif 50 < x_m < 350 and 720 < y_m < 770:
         pygame.draw.rect(screen, (255,0,0), (50, 720, 300, 50), 6)
         if mb[0] == True:
             exit()


def main():
    pygame.init()

    res = (1280, 800)
    screen = pygame.display.set_mode(res)
    image = pygame.image.load("Title_shufle_1.png")
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
        #background color
        screen.fill((214,200,170))

        Menu_inicial(screen)
        screen.blit(image, (250,100))

        pygame.display.flip()
       


main()
