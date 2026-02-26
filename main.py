import pygame
from constants import WIDTH, HEIGHT, ROWS, COLS, CELL_SIZE, BACKGROUND_COLOR, GRID_LINE_COLOR, FPS, LIVE_CELL_COLOR
from cell import Cell
import time
def draw_grid(surface):
    
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRID_LINE_COLOR, (x, 0), (x, HEIGHT), 2)
    
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRID_LINE_COLOR, (0, y), (WIDTH, y), 2)

def count_neighbours(board, cell, x, y):
    coordinate_offset = [[-1,-1],[0,-1],[+1,-1],[-1,0],
                         [+1,0],[-1,+1],[0,+1],[+1,+1]]
    count = 0
    for coor in coordinate_offset:
        offset_y = coor[1]
        offset_x = coor[0]
        
        
        if y + (offset_y) < 0 or x + (offset_x) < 0:
            continue
        if y + (offset_y) >= ROWS or x + (offset_x) >= COLS: 
            continue
        else:
            ix = x + (offset_x)
            iy = y + (offset_y) 
            if board[iy][ix].is_alive:
                
                count += 1
    cell.neighbour_count = count
    return count
            

def main():
    pygame.init()

    pygame.display.set_caption("Conway's Game of Life")
    
    window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(pygame.Color(BACKGROUND_COLOR))
    board = [[Cell() for _ in range(COLS)] for _ in range(ROWS)]
    clock = pygame.time.Clock()
    draw_value = False
    is_drawing = False
    
    
    frame_count = 0
    is_paused = True
    is_running = True
    
    while is_running:
        frame_count += 1 
        if frame_count >= FPS:
            frame_count = 0
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused
            
            if event.type == pygame.MOUSEBUTTONUP:
               is_drawing = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // CELL_SIZE
                col = mouse_x // CELL_SIZE
                if board[row][col].is_alive == True:
                    draw_value = False
                if board[row][col].is_alive == False:
                    draw_value = True
                is_drawing = True
                    
        if is_drawing == True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // CELL_SIZE
            col = mouse_x // CELL_SIZE
            board[row][col].is_alive = draw_value
        

        
            
            
            
        if not is_paused:
            if frame_count % 5 == 0:
                # Esto es la parte de preparacion PHASE 1:         
                for y, row in enumerate(board):
                    for x, cell in enumerate(row):
                        count_neighbours(board, cell, x, y)
                        cell.prepare_next_gen()
        
                #Esta se supone que es donde se actualize PHASE 2:
                for row in board:
                    for cell in row:
                        cell.update()
            
  
        #Esta se supone que es ahora donde se dibuja lo que ya se calculo PHASE 3:
        for iy, row_of_cells in enumerate(board):
            for ix, cell in enumerate(row_of_cells):
                color = ((LIVE_CELL_COLOR) if cell.is_alive else (BACKGROUND_COLOR))
                pygame.draw.rect(window_surface,color, (ix*CELL_SIZE, iy*CELL_SIZE, CELL_SIZE, CELL_SIZE) )
       
        
                    
                
        draw_grid(window_surface)
        pygame.display.update()
        
        

    
if __name__ == "__main__":
    main()