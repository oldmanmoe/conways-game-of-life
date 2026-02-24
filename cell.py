
class Cell:
    def __init__(self):
        
        self.x = None
        self.y = None
        self.is_alive = False
        self.neighbour_count = None
        self.next_state = None
    
    def assign_pos(self,x,y):
        self.x = x
        self.y = y
    
    def prepare_next_gen(self, cell):
        if cell.is_alive:
            if cell.neighbour_count < 2:
                cell.next_state = False
                return
            elif cell.neighbour_count > 3:
                cell.next_state = False
                return
            else:
                cell.next_state = False
                return
        else:
            if cell.neighbour_count == 3:
                cell.next_state = True
                return
            cell.next_state = False
            return 
        
                
    def update(self): 
        pass

