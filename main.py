import pygame
import constants

def draw_grid(surface):
    
    for x in range(0, constants.WIDTH, constants.CELL_SIZE):
        pygame.draw.line(surface, constants.GRID_LINE_COLOR, (x, 0), (x, constants.HEIGHT))
    
    for y in range(0, constants.HEIGHT, constants.CELL_SIZE):
        pygame.draw.line(surface, constants.GRID_LINE_COLOR, (0, y), (constants.WIDTH, y))
    
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
        draw_grid(window_surface)
        pygame.display.update()
        

    
if __name__ == "__main__":
    main()