import pygame 
import pygame.freetype


def figuras(screen):
     my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 30)
     i = 0
     y = 350
         
     while i < 6:
         pygame.draw.rect(screen, (204,86,0), (490, y, 300, 50), 6)
         my_font.render_to(screen, (610, y + 15), "3 X 4", (128,53,0))
         y += 60
         i += 1

     pygame.draw.rect(screen, (204,86,0), (50, 720, 300, 50), 6)
     my_font.render_to(screen, (175, 735), "EXIT", (128,53,0))

def main():
    pygame.init()
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 30)

    res = (1280, 800)
    screen = pygame.display.set_mode(res)
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
        #background color
        screen.fill((166,127,99))

        figuras(screen)
        #if 490 < pygame.mouse.get_pos()[0] < 790 and 350 < pygame.mouse.get_pos()[1] < 400:
         #   pygame.draw.rect(screen, (0,86,0), (490, 350, 300, 50), 6)
          #  my_font.render_to(screen, (610, 365), "3 X 4", (128,53,0))

        pygame.display.flip()
       


main()
