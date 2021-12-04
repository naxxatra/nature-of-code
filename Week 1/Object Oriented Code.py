import pygame
import random
import numpy as np

delta_t = 0.1
dimensions = [1000,500]

class ball:

    def __init__(self, radius, position, velocity, acceleration):
        #Taking Radius, Position, velocity, acceleration as inputs and making them object variables
        self.radius = radius
        self.pos = np.asarray(position)
        self.vel = np.asarray(velocity)
        self.acc = acceleration
        #Randomly generating the RGB values for the object colour
        r = random.randint(0,255)
        b = random.randint(0,255)
        g = random.randint(0,255)
        self.color = (r,g,b)

    def collide(self):
            x,y = self.pos

            '''Collision logic is still the same as the other program. Refer to comments there'''
            if y<=0 or y>=dimensions[1]:
                self.vel += self.acc*np.asarray([0,delta_t]) #Special Hack
                self.vel = self.vel*np.asarray([1,-1])

            if x<=0 or x>= dimensions[0]:
                self.vel += np.asarray([delta_t, 0]) #Special Hack
                self.vel = self.vel*np.asarray([-1,1])

    def update(self):
        '''Update logic is still the same as the other program. Refer to the comments there'''
        self.vel = self.vel + self.acc * delta_t
        self.pos = self.pos + self.vel * delta_t
        self.collide()

    def draw(self):
        '''Update logic is still the same as the other program. Refer to the comments there'''
        self.update()
        pygame.draw.circle(win, self.color, self.pos, self.radius)


#Making a list called my_balls where the balls are stored
my_balls = []
number_of_balls = 2
#Iterating number_of_balls times and making a new ball, and appending it to the list
for i in range(number_of_balls):
    #Randomly generating position and velocity
    pos = [random.randint(0,dimensions[0]), random.randint(0,dimensions[1])]
    vel = [random.random(), random.random()]
    #Random radius between 5 and 10
    radius = random.randint(5,10)
    #making a ball
    i_th_ball = ball(radius, pos, vel, [0,0])
    #Appending the ball to the list
    my_balls.append(i_th_ball)



pygame.init()

win = pygame.display.set_mode(dimensions)
fpsClock = pygame.time.Clock()

run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            pass


    win.fill((0,0,0)) #painting the window black
    #Iterating through the list of balls we have
    for i_ball in my_balls:
        i_ball.draw() #Drawing each ball to the screen



    pygame.display.flip() #Updating the screen
    fpsClock.tick(600)

pygame.quit()
