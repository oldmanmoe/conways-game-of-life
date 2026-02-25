
class Cell:
    def __init__(self):

        self.is_alive = False
        self.neighbour_count = None
        self.next_state = None

    def prepare_next_gen(self,):
        if self.is_alive:
            if self.neighbour_count == 2 or self.neighbour_count == 3:
                self.next_state = True
                return
            else:
                self.next_state = False
                return
        else:
            if self.neighbour_count == 3:
                self.next_state = True
                return
            self.next_state = False
            return 
        
                
    def update(self): 
        if self.next_state is not None:
            self.is_alive = self.next_state
            self.next_state = None
