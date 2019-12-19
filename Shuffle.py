import pygame 

def main():
    pygame.init()

    res = (640, 360)
    screen = pygame.display.set_mode(res)

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()




main()
