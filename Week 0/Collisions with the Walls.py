#Importing the Libraries
import pygame
import random
import numpy as np


#Default values for the Position, Velocity, and Acceleration
pos = np.asarray([100,100])
vel = np.asarray([0.5,3])
acc = np.asarray([0,1])

'''We're using Euler's Method of Integration in this code. So we're defining a time
step that can be adjusted. The smaller the timestep, the more accurate our code.'''
delta_t = 0.1

def draw(): #The Draw function is called Each Iteration to update the frame
    global win, colour, pos #Taking the nessecary global variables
    win.fill((0,0,0)) #Painting the screen Black. comment out this line to visualize the path of the particle

    update() #Update function updates the values of position and velocity before drawing them to the screen
    '''pygame.draw.circle takes in 4 inputs to draw a circle.
    1. Surface: The window where we're drawing the circle to
    2. Color: The colour of the ball
    3. Position: The x and y coordinates of the circle
    4. Radius: The radius of the ball
    '''
    pygame.draw.circle(win, colour, pos ,10)

def update(): #The function called before drawing. The one where we're updating the values of position, velocity.
    global pos, vel, acc, delta_t #Taking the nessecary global variables
    vel = vel + acc*delta_t #Velocity is updated according to euler's method.
    pos = pos + vel*delta_t #Position is updated according to euler's method.
    collide() #Updating the values according to the any collisions we're doing


def collide(): #Colliding with the walls and updating the values accordingly.
    global pos, vel,delta_t #Taking the nessecary global variables
    x,y = pos #Splitting the position vector into local variables that's easier to work with
    '''Explanation of the special hack
    Each time the ball bounces, it is observed that the velocity of the ball is decreasing by delta_t*acc
    To account for this, we're hacking and adding the lost velocity at the time of bounce.
    The decrease is because of the errors coming from the way we're integrating the diffrential equations
    of position velocity and acceleration.

    A better solution would be to use a better method of integrating but :)
    '''

    if y<=0 or y>=dimensions[1]:  #Checking if the ball went out of the bounds of the window
        vel += acc*np.asarray([0,delta_t]) #Special Hack
        vel = vel*np.asarray([1,-1]) #Reversing the specific component of the velocity

    if x<=0 or x>= dimensions[0]: #Checking if the ball went out of the bounds of the window
        vel += acc*np.asarray([delta_t, 0]) #Special Hack
        vel = vel*np.asarray([-1,1]) #Reversing the specific component of the velocity


#Randomly generating the r,g,b values of the colour of our ball.
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
colour = (r,g,b)



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
