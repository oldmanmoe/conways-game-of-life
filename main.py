import pygame
from constants import WIDTH, HEIGHT, ROWS, COLS, CELL_SIZE, BACKGROUND_COLOR, GRID_LINE_COLOR, FPS, LIVE_CELL_COLOR
from cell import Cell

def draw_grid(surface):
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRID_LINE_COLOR, (x, 0), (x, HEIGHT), 2)
    
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRID_LINE_COLOR, (0, y), (WIDTH, y), 2)
        

    
def main():
    pygame.init()

    pygame.display.set_caption("Conway's Game of Life")
    
    window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(pygame.Color(BACKGROUND_COLOR))
    board = [[Cell() for _ in range(COLS)] for _ in range(ROWS)]
    clock = pygame.time.Clock()
    
    
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    row = event.pos[1] // CELL_SIZE
                    col = event.pos[0] // CELL_SIZE
                    board[row][col].is_alive = not board[row][col].is_alive
                
                
        for iy, row_of_cells in enumerate(board):
            for ix, cell in enumerate(row_of_cells):
                color = ((LIVE_CELL_COLOR) if cell.is_alive else (BACKGROUND_COLOR))
                pygame.draw.rect(window_surface,color, (ix*CELL_SIZE, iy*CELL_SIZE, CELL_SIZE, CELL_SIZE) )

                    
                      
    
    
        
        
        draw_grid(window_surface)
        pygame.display.update()
        clock.tick(FPS)
        

    
if __name__ == "__main__":
    main()