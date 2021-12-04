#Importing the Library, Pygame. Can be installed by `pip install pygame.`
import pygame

def draw(): #This is the function we'll be using to draw each frame.
    pass


pygame.init() #Intializing the pygame engine

dimensions = [1000, 500] #Setting a tuple of x and y dimensions for the window

#Making a pygame window where we will be drawing stuff
win = pygame.display.set_mode(dimensions) 

'''fpsClock is basically a Clock that lets you control how fast the 
The program is going to be running'''
fpsClock = pygame.time.Clock() #Basically a clock.

run = True #Run is a variable that we can set to false when we want the window to close

while run: #As long as this while loop is true, we can see the window
    '''Pygame stores any interactions with the screen in a queue called 
	pygame.event.get(). We are going through that queue and looking for a specific
	event called pygame.QUIT, which is triggered when you press the x button in the
	window. When we set run to False, the while loop, and hence the window will 
	close'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            pass
    #Drawing to the screen each iteration
    draw()
    #Updating the display to reflect the changes made in the new frame
    pygame.display.flip()
    #Telling the clock to pause the code for 1/60th of a second, and then go ahead
    fpsClock.tick(60)

#We're out of the while loop, so it assumes we're done with the code.
#Might as well close the engine we intialized at the start of the code.
pygame.quit()