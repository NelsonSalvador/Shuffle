import pygame
import random


class Levels_gameplay:
    def __init__(self, screen, level):
        self.level = level
        self.screen = screen
    def game(self, screen, level):
     m = 0
     clicked = []
     jogo = []
     clicked_i = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,
     False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
     jogo_i = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18]
     ver = []

     if level == 1:
         while m < 12:
            clicked.append(clicked_i[m])
            jogo.append(jogo_i[m])
            m += 1 
     if level == 2:
         while m < 16:
            clicked.append(clicked_i[m])
            jogo.append(jogo_i[m])
            m += 1 
     if level == 3:
         while m < 20:
            clicked.append(clicked_i[m])
            jogo.append(jogo_i[m])
            m += 1 
     if level == 4:
         while m < 24:
            clicked.append(clicked_i[m])
            jogo.append(jogo_i[m])
            m += 1 
     if level == 5:
         while m < 30:
            clicked.append(clicked_i[m])
            jogo.append(jogo_i[m])
            m += 1 
     if level == 6:
         while m < 36:
            clicked.append(clicked_i[m])
            jogo.append(jogo_i[m])
            m += 1 
     for i in range(0, m + 1):
         random.shuffle(jogo)
     Set_t = set()
     while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
         
        x_m = pygame.mouse.get_pos()[0]
        y_m = pygame.mouse.get_pos()[1]
        mb = pygame.mouse.get_pressed()
        screen.fill((214,200,170))
        my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

        i = 0
        x = 420
        y = 80
        j = 0
        

        if level == 1:
            
            while i < 12:
                if i not in Set_t:
                    pygame.draw.rect(screen, (150,0,0), (x + 70, y + 60, 80, 120), 0)
                    if x + 70 < x_m < x + 70 + 80 and y + 60 < y_m < y + 60 + 120:
                        pygame.draw.rect(screen, (255,0,0), (x + 70, y + 60, 80, 120), 3)
                        if mb[0] == True:
                           clicked[i] = True
                           pygame.time.wait(50)
    
                    if (clicked[i]):
                        if jogo[i] == 1:
                            pygame.draw.rect(screen, (0,150,0), (x + 70, y + 60, 80, 120), 0)
                        elif jogo[i] == 2:
                            pygame.draw.rect(screen, (0,150,150), (x + 70, y + 60, 80, 120), 0)
                        elif jogo[i] == 3:
                            pygame.draw.rect(screen, (150,150,150), (x + 70, y + 60, 80, 120), 0)
                        elif jogo[i] == 4:
                            pygame.draw.rect(screen, (0,214,150), (x + 70, y + 60, 80, 120), 0)
                        elif jogo[i] == 5:
                            pygame.draw.rect(screen, (0,150,214), (x + 70, y + 60, 80, 120), 0)
                        elif jogo[i] == 6:
                            pygame.draw.rect(screen, (214,150,150), (x + 70, y + 60, 80, 120), 0)
                i += 1
                if i == 3 or i == 6 or i == 9 or i == 12:
                    x = 420 
                    y += 140
                else :
                    x += 100

            while j < 12:
                if(clicked[j]):
                    ver.append(jogo[j])
                    ver.append(j)
                    j += 1
                    while j < 12:
                        if (clicked[j]):
                            ver.append(jogo[j])
                            ver.append(j)
                        j += 1
                j += 1
            if len(ver) <= 2:
        
                ver.clear() 
            elif ver[0] != ver[2]:
                clicked = [False,False,False,False,False,False,False,False,False,False,False,False]
                print(ver)
                ver.clear()
            elif ver[0] == ver[2]:
                Set_t.add(ver[1])
                Set_t.add(ver[3])
                clicked = [False,False,False,False,False,False,False,False,False,False,False,False]
                print(ver)
                ver.clear()
            

        if level == 2:
            while i < 16:
                 pygame.draw.rect(screen, (150,0,0), (x + 35, y + 60, 80, 120), 0)
                 i += 1
                 if i == 4 or i == 8 or i == 12 or i == 16:
                     x = 420 
                     y += 140
                 else :
                     x += 100
            i = 0
            while i < 16:
                if x + 35 < x_m < x + 35 + 80 and y + 60 < y_m < y + 60 + 120:
                    pygame.draw.rect(screen, (0,0,150), (x + 35, y + 60, 80, 120), 0)
                    if mb[0] == True:
                        pygame.draw.rect(screen, (0,150,0), (x + 35, y + 60, 80, 120), 0)
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
            while i < 16:
                if x < x_m < x + 80 and y + 60 < y_m < y + 60 + 120:
                    pygame.draw.rect(screen, (0,0,150), (x, y + 60, 80, 120), 0)
                    if mb[0] == True:
                        pygame.draw.rect(screen, (0,150,0), (x, y + 60, 80, 120), 0)
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
            if mb[0] == True:
                return 0
        pygame.display.flip()
