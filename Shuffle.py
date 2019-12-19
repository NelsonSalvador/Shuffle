import pygame 

def main():
    pygame.init()
    res(640, 360)
    screen = pygame.display.set_mode(res)

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()


        screen.fill((0,0,20))
        pygame.draw.circle(screen, (255,255,0), (320, 180), 20, 5)
        pygame.display.flip()


main()
