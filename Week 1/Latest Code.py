import pygame
import random
import numpy as np

'''This is the latest version of the Non-Object Oriented version of a single particle moving.
For proper line by line comments, refer to the code in week 0. It's basically the same thing rearranged'''

pos = np.asarray([200,200])
vel = np.asarray([1,2])
acc = np.asarray([0,3])

delta_t = 0.1

def collide():
    global pos, vel,delta_t
    x,y = pos

    if y<=0 or y>=dimensions[1]:
        vel += acc*np.asarray([0,delta_t]) #Special Hack
        vel = vel*np.asarray([1,-1])

    if x<=0 or x>= dimensions[0]:
        vel += acc*np.asarray([delta_t, 0]) #Special Hack
        vel = vel*np.asarray([-1,1])





def update():
    global pos, vel, acc, delta_t
    vel = vel + acc*delta_t
    pos = pos + vel*delta_t
    collide()



def draw():
    global win, colour, pos
    #win.fill((0,0,0))

    update()
    pygame.draw.circle(win, (255,255,255), (100,100), 10)
    pygame.draw.circle(win, colour, pos ,10)

pygame.init()

dimensions = [1000,500]
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
colour = (r,g,b)



win = pygame.display.set_mode(dimensions)
fpsClock = pygame.time.Clock()

run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            pass

    draw()
    pygame.display.flip()
    fpsClock.tick(600)

pygame.quit()
