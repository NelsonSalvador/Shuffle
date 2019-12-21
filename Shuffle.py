import pygame 
import pygame.freetype


def Menu_inicial(screen):
     my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 30)
     i = 0
     y = 350
     l1 = 3
     l2 = 4 
     level = 0
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
             levels(screen, level)

     elif 490 < x_m < 790 and 410 < y_m < 460:
         pygame.draw.rect(screen, (255,0,0), (490, 410, 300, 50), 6)
         if mb[0] == True:
             level = 2
             levels(screen, level)
    
     elif 490 < x_m < 790 and 470 < y_m < 520:
         pygame.draw.rect(screen, (255,0,0), (490, 470, 300, 50), 6)
         if mb[0] == True:
             level = 3
             levels(screen, level)

     elif 490 < x_m < 790 and 530 < y_m < 580:
         pygame.draw.rect(screen, (255,0,0), (490, 530, 300, 50), 6)
         if mb[0] == True:
             level = 4
             levels(screen, level)
    
     elif 490 < x_m < 790 and 590 < y_m < 640:
         pygame.draw.rect(screen, (255,0,0), (490, 590, 300, 50), 6)
         if mb[0] == True:
             level = 5
             levels(screen, level)
    
     elif 490 < x_m < 790 and 650 < y_m < 700:
         pygame.draw.rect(screen, (255,0,0), (490, 650, 300, 50), 6)
         if mb[0] == True:
             level = 6
             levels(screen, level)
    
     elif 50 < x_m < 350 and 720 < y_m < 770:
         pygame.draw.rect(screen, (255,0,0), (50, 720, 300, 50), 6)
         if mb[0] == True:
             exit()

def levels(screen, level):
    while (True):
         for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
         
         screen.fill((214,200,170))
         my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 30)
         i = 0
         x = 420
         y = 80

         mb_levels = pygame.mouse.get_pressed()
         # desenha as cartas conforme os níveis
         if level == 1:
             while i < 12:
                 pygame.draw.rect(screen, (150,0,0), (x + 70, y + 60, 80, 120), 0)
                 i += 1
                 if i == 3 or i == 6 or i == 9 or i == 12:
                     x = 420 
                     y += 140
                 else :
                     x += 100
         if level == 2:
             while i < 16:
                 pygame.draw.rect(screen, (150,0,0), (x + 35, y + 60, 80, 120), 0)
                 i += 1
                 if i == 4 or i == 8 or i == 12 or i == 16:
                     x = 420 
                     y += 140
                 else :
                     x += 100
         if level == 3:
             while i < 20:
                 pygame.draw.rect(screen, (150,0,0), (x, y + 60, 80, 120), 0)
                 i += 1
                 if i == 5 or i == 10 or i == 15 or i == 20:
                     x = 420 
                     y += 140
                 else :
                     x += 100
         if level == 4:
             while i < 24:
                 pygame.draw.rect(screen, (150,0,0), (x - 35, y + 60, 80, 120), 0)
                 i += 1
                 if i == 6 or i == 12 or i == 18 or i == 24:
                     x = 420 
                     y += 140
                 else :
                     x += 100  
         if level == 5:
             while i < 30:
                 pygame.draw.rect(screen, (150,0,0), (x - 35, y, 80, 120), 0)
                 i += 1
                 if i == 6 or i == 12 or i == 18 or i == 24 or i == 30:
                     x = 420 
                     y += 140
                 else :
                     x += 100 
         if level == 6:
             while i < 36:
                 pygame.draw.rect(screen, (150,0,0), (x, y, 70, 105), 0)
                 i += 1
                 if i == 6 or i == 12 or i == 18 or i == 24 or i == 30:
                     x = 420 
                     y += 115
                 else :
                     x += 80                   


         pygame.draw.rect(screen, (150,0,0), (50, 720, 300, 50), 6)
         my_font.render_to(screen, (175, 735), "EXIT", (128,53,0))

         if 50 < pygame.mouse.get_pos()[0] < 350 and 720 < pygame.mouse.get_pos()[1] < 770:
            pygame.draw.rect(screen, (255,0,0), (50, 720, 300, 50), 6)
            if mb_levels[0] == True:
             main()

         pygame.display.flip()


def main():
    pygame.init()

    res = (1280, 800)
    screen = pygame.display.set_mode(res)
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
        #background color
        screen.fill((214,200,170))

        Menu_inicial(screen)

        pygame.display.flip()
       


main()
