import pygame, sys, math, random, time
# Maze generation algorithm using Depth First Search and Recursive Backtracking
# Alex Reyes Summer 2023

#Journal:
""" 6/8 - walls are not visually being removed. pretty sure they are being removed in the code tho...
    6/9 - something is probably wrong with how I made my grid. I have a feeling cells aren't where they are supposed to be...
    6/12 - removing the walls is still not working. The grid doesnt seem to be the problem. Right now I think it could be
    the drawGrid() function constantly being called. Because within that the show function is being called which is responsible
    for drawing the walls on the grid.


    
"""

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
cell_size = 40

columns = math.floor(WINDOW_WIDTH/cell_size) # var
rows = math.floor(WINDOW_HEIGHT/cell_size) # var

grid = [] # 1D Array(List) to store all the cells v a r

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

    def getCoords(self):
        return self.i, self.j
    
    def highlight(self):
        x = self.i * cell_size
        y = self.j*cell_size

        rect = pygame.Rect(x,y, cell_size, cell_size)
        pygame.draw.rect(SCREEN, "white",rect, 0)
    
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
            #Line Bottom
            pygame.draw.line(SCREEN, "green", (x,y),(x+cell_size,y),2)
        else:
            print("no")
            

        if self.walls[1]:
            #Line Right
            pygame.draw.line(SCREEN, "green", (x+cell_size,y),(x+cell_size, y+cell_size),2)
        else:
            print("no")
            

        if self.walls[2]:
            #Line Left
            pygame.draw.line(SCREEN, "green", (x,y),(x,y+cell_size),2)
        else:
            print("no")
            

        if self.walls[3]:
            #Line Top
            pygame.draw.line(SCREEN, "green", (x,y+cell_size),(x+cell_size,y+cell_size),2)
        else:
            print("no")
            
       # if self.visited:
            #rect = pygame.Rect(x,y,cell_size,cell_size)
            #pygame.draw.rect(SCREEN, "grey ", rect,-1)
 
        
    def checkNeighbors(self):
        neighbors = []

        #these are cells(objects)
        top = grid[index(self.i,self.j-1)]
        bottom = grid[index(self.i, self.j+1)]
        right = grid[index(self.i+1, self.j)]
        left = grid[index(self.i-1, self.j)]

        #sides = [bottom, right, left, top]


        #for n in sides:
            #if n and not n.visited:
             #   neighbors.append(n)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if right and not right.visited:
            neighbors.append(right)
        if left and not left.visited:
            neighbors.append(left)
        if top and not top.visited:
            neighbors.append(top)


        if len(neighbors) > 0:
            r = random.randint(0, len(neighbors)-1) # has to be -1 because random function is (inclusive, inclusive)
            return neighbors[r]
        else:
            return None






def drawGrid():
    global current
    for s in grid:
        s.show() 
    current.visited = True
    #current.highlight()

    next_cell = current.checkNeighbors()

    if next_cell is not None:
        next_cell.visited = True

        removeWalls(current, next_cell)
    current = next_cell



    
    
    #print("DRAW") being called the whole time the loop is on


    

    #current.visited = True
    #next = current.checkNeighbors()
    #if next:
      #  next.visited = True
     #   current = next

def removeWalls(a,b):
    #a, b are cell 
    #change = a - b(a is a, b b)
    delta_x = a.i - b.i

    if delta_x == 1:
        a.walls[2] = False # L
        b.walls[1] = False # R
    elif delta_x == -1:
        a.walls[1] = False # R
        b.walls[2] = False# L

    
    delta_y = a.j - b.j

    if delta_y == 1:
        a.walls[3] = False # T
        b.walls[0] = False # B

    elif delta_y == -1:
        a.walls[0] = False # B
        b.walls[3] = False # T




def main():
    global SCREEN,CLOCK,current
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill("black")
    

    current = grid[0]
    


    while True:
        
        #time.sleep(0.25)
        
        drawGrid()
        #current.visited = True
        #current.highlight()

        #next_cell = current.checkNeighbors()

        #if next_cell is not None:
            #next_cell.visited = True
            #removeWalls(current, next_cell)
            #time.sleep(1)
        #current = next_cell
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            

        pygame.display.update()
        #drawGrid()
        #--inside
        #current.visited = True

        #next = current.checkNeighbors()

        #if next:
         #   next.visited = True
            #push the current cell to the stack
          #  removeWalls(current, next)

            #--remove the wall between the current cell and the choose cell
           # current = next
            #--print(current.getCoords())
        #--inside end
        

        #time.sleep(0.25)
       # for z in grid:
         #   for i in range(3):
         #       z.walls[i] = False
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                current.visited = True

                next_cell = current.checkNeighbors()

                print(f"current cell: {current.getCoords()}")
                print(f"next_cell: {next_cell.getCoords()}")

                if next_cell is not None:
                    next_cell.visited = True
                    removeWalls(next_cell, current)
                    current = next_cell
                drawGrid()
                pygame.display.update()"""
            
                

setup()
print("Start Maze")
main()

