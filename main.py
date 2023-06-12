import pygame, sys, math, random, time
# Maze generation algorithm using Depth First Search and Recursive Backtracking
# Alex Reyes Summer 2023

#Journal:
""" 6/8 - walls are not visually being removed. pretty sure they are being removed in the code tho...
    6/9 - something is probably wrong with how I made my grid. I have a feeling cells aren't where they are supposed to be...


    
"""

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
cell_size = 40

columns = math.floor(WINDOW_WIDTH/cell_size) # var
rows = math.floor(WINDOW_HEIGHT/cell_size) # var

grid = [] # 1D Array(List) to store all the cells v a r

def setup():
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
        self.walls = [False, True, True, True]
        self.visited = False

    def getCoords(self):
        return self.i, self.j
    
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
            pygame.draw.line(SCREEN, "white", (x,y),(x+cell_size,y),1)

        if self.walls[1]:
            #Line Right
            pygame.draw.line(SCREEN, "white", (x+cell_size,y),(x+cell_size, y+cell_size),1)

        if self.walls[2]:
            #Line Left
            pygame.draw.line(SCREEN, "white", (x,y),(x,y+cell_size),1)

        if self.walls[3]:
            #Line Top
            pygame.draw.line(SCREEN, "white", (x,y+cell_size),(x+cell_size,y+cell_size),1)
        if self.visited:
            rect = pygame.Rect(x,y,cell_size,cell_size)
            pygame.draw.rect(SCREEN, "grey ", rect,0)
    def checkNeighbors(self):
        neighbors = []

        #these are cells(objects)
        top = grid[index(self.i,self.j-1)]
        bottom = grid[index(self.i, self.j+1)]
        right = grid[index(self.i+1, self.j)]
        left = grid[index(self.i-1, self.j)]

        sides = [bottom, right, left, top]



        #sides = [top, right, bottom, left]
        for n in sides:
            print(f'n-cell is visited?: {n.visited}')
            if n and not n.visited:
                neighbors.append(n)
        print(len(neighbors))

                #print(f'Added: {n} to neighbors, which is {len(neighbors)} long')



        if len(neighbors) > 0:
            r = random.randint(0, len(neighbors)-1) # has to be -1 because random function is (inclusive, inclusive)
            #print(len(neighbors))
            return neighbors[r]
        else:
            return None







def drawGrid():
    for s in range(len(grid)):
        grid[s].show() 


    

    #current.visited = True
    #next = current.checkNeighbors()
    #if next:
      #  next.visited = True
     #   current = next

def removeWalls(final,initial):
    #a, b are cell 
    #change = final - initial(a is final, b initial)
    delta_x = final.i - initial.i

    if delta_x == 1:
        final.walls[2] = False # L
        initial.walls[1] = False # R
    elif delta_x == -1:
        final.walls[1] = False # R
        initial.walls[2] = False# L
    
    delta_y = final.j - initial.j

    if delta_y == 1:
        final.walls[3] = False # T
        initial.walls[0] = False # B
    elif delta_y == -1:
        final.walls[0] = False # B
        initial.walls[3] = False # T


def main():
    global SCREEN, CLOCK, current
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill("black")

    setup()
    current = grid[0]
    current.visited = True


    while True:
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
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print("chnaged to true")

                next_cell = current.checkNeighbors()

                if next_cell is not None:
                    next_cell.visited = True
                    removeWalls(current, next_cell)
                    current = next_cell
            
                print(f'current{current.walls}')
                print(f'next{next_cell.walls}')

        
            
        drawGrid()
        pygame.display.update()

print("Start Maze")
main()

