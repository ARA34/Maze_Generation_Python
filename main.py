import pygame, sys, math, random
# Maze generation algorithm using pygame in python
# Alex R Summer 2023

#changelog
""" 
    6/8 - Bruh I should have saved my previous github, now my notes from there are gone...
    Walls are not visually being removed. pretty sure they are being removed in the code tho...
    6/9 - something is probably wrong with how I made my grid. I have a feeling cells aren't where they are supposed to be...
    6/12 - removing the walls is still not working. The grid doesnt seem to be the problem. Right now I think it could be
    the drawGrid() function constantly being called. Because within that the show function is being called which is responsible
    for drawing the walls on the grid.
    6/13 - github comment was: still working...
    6/15 - NO WAY! I think I fixed the walls issue... I was simply mistaking the bottom for the top and vice versa...
    SMH
"""

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
cell_size = 40


columns = math.floor(WINDOW_WIDTH/cell_size) # var
rows = math.floor(WINDOW_HEIGHT/cell_size) # var

grid = [] # 1D Array(List) to store all the cells v a r
output_grid = [] #1D array to output at the end

stack = []

def setup(): #this is only being called once at the beginning
    for j in range(rows):
        for i in range(columns):
            cell = Cell(i,j)
            grid.append(cell)

def index(i,j):
    if i < 0 or j < 0 or i > columns - 1 or j > rows - 1:
        return -1
    else:
        return i + j * columns

class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j   
        self.walls = [True, True, True, True]
        self.visited = False
        self.visited_color = "black"
        self.leading_color = "grey"

    def wallStatus(self):
        print(f"Walls: {self.walls}")

    def getCoords(self):
        return self.i, self.j
    
    def lead(self):
        x = self.i * cell_size
        y = self.j*cell_size

        rect = pygame.Rect(x,y, cell_size, cell_size)
        pygame.draw.rect(SCREEN, self.leading_color,rect, 0)
    
    def show(self):
        x = self.i * cell_size
        y = self.j * cell_size
        #rect = pygame.Rect(x,y, cell_size, cell_size)
        #pygame.draw.rect(SCREEN, "white",rect, 1)
        
        #    __
        #   |  |  Cell Box
        #    -- 
        #Bottom, Right, Left, Top


        if self.walls[0]:
            #Line Top
            pygame.draw.line(SCREEN, "green", (x,y),(x+cell_size,y),2)            

        if self.walls[1]:
            #Line Right
            pygame.draw.line(SCREEN, "green", (x+cell_size,y),(x+cell_size, y+cell_size),2)
        
            

        if self.walls[2]:
            #Line Left
            pygame.draw.line(SCREEN, "green", (x,y),(x,y+cell_size),2)
    
            

        if self.walls[3]:
            #Line Bottom
            pygame.draw.line(SCREEN, "green", (x,y+cell_size),(x+cell_size,y+cell_size),2)
        
            
        if self.visited:
            rect = pygame.Rect(x,y,cell_size,cell_size)
            pygame.draw.rect(SCREEN, self.visited_color, rect,-1)
 
        
    def checkNeighbors(self):
        neighbors = []

        #these are cells(objects)
        top = grid[index(self.i,self.j-1)]
        bottom = grid[index(self.i, self.j+1)]
        right = grid[index(self.i+1, self.j)]
        left = grid[index(self.i-1, self.j)]

        #sides = [bottom, right, left, top]
        sides = [top, right, left, bottom]


        for n in sides:
            if n and not n.visited:
                neighbors.append(n)


        if len(neighbors) > 0:
            r = random.randint(0, len(neighbors)-1) # has to be -1 because random function is (inclusive, inclusive)
            return neighbors[r]
        else:
            return None


#DRAWGRID
def drawGrid():
    global current,next_cell
    for s in grid:
        s.show() 
    current.visited = True
    current.lead()
    

    next_cell = current.checkNeighbors()

    if next_cell is not None:
        next_cell.visited = True 

        stack.append(current)
        removeWalls(current, next_cell)
        current = next_cell
    elif len(stack) > 0:
        current = stack.pop()
        
def removeWalls(a,b):
    #a, b are cell 
    delta_x = a.i - b.i

    if delta_x == 1:
        a.walls[2] = False # L
        b.walls[1] = False # R


    elif delta_x == -1:
        a.walls[1] = False # R
        b.walls[2] = False# L

    delta_y = a.j - b.j

    if delta_y == 1:
        a.walls[0] = False # T
        b.walls[3] = False # B

    elif delta_y == -1:
        a.walls[3] = False # B
        b.walls[0] = False # T




def main():
    global SCREEN,CLOCK,current
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill("black")
    
    setup()
    current = grid[0]
    


    while True:
        all_visited = all(s.visited == True for s in grid)
        if not all_visited:
            drawGrid()
        elif all_visited:
            for s in grid:
                s.leading_color = "black"
                s.lead()
            grid[0].walls[1] = False
            grid[1].walls[2] = False
            grid[10].walls[0] = False
            drawGrid()         

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    SCREEN.fill("black")
                    
        pygame.display.update()
                     

print("--------------------Start Maze Generation--------------------")
main()

