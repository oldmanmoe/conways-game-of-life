import pygame
import constants

def main():
    
    pygame.init()

    pygame.display.set_caption("Conway's Game of Life")
    window_surface = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    background = pygame.Surface((constants.WIDTH, constants.HEIGHT))
    background.fill(pygame.Color(constants.BACKGROUND_COLOR))
    
    is_running = True

    while is_running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
    
        window_surface.blit(background, (0, 0))
    
        pygame.display.update()
 
    
if __name__ == "__main__":
    main()