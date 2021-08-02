import pygame
from pygame.locals import *
import math as m

class char :
    def __init__(self, r, v) :
        self.r = r
        self.θ = 0
        self.v = v
        self.direction = 'none'
        self.coords = (int(250 + self.r*m.cos(self.θ)), int(250 + self.r*m.sin(self.θ)))

    def move(self) :
        if self.direction == 'out' :
            self.r += self.v*dt
        if self.direction == 'in' and self.r > self.v*dt :
            self.r -= self.v*dt
        if self.direction == 'ccw' :
            self.θ -= (ω(self)*dt)
        if self.direction == 'cw' :
            self.θ += (ω(self)*dt)
        self.coords = (int(250 + self.r*m.cos(self.θ)), int(250 + self.r*m.sin(self.θ)))
    
def ω(char):
    return char.v/char.r

def printScreen(surface, mouse, cat) :
    fenetre.fill((255, 255, 255))
    pygame.draw.circle(surface, (150, 150, 255), (250, 250), 200)
    pygame.draw.circle(surface, (0, 0, 0), (250, 250), 1)
    pygame.draw.circle(surface, (0, 0, 0), cat.coords, 4)
    pygame.draw.circle(surface, (100, 100, 100), mouse.coords, 2)
    
    pygame.display.flip()

mouse0 = char(5, 0.3)
cat = char(200, 1.2)
dt = 1

pygame.init()
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode ((500, 500))
surface = pygame.display.get_surface()
pygame.key.set_repeat(50, 50)
run = True
end = False

while run :
    clock.tick(1/dt*1000)
    keys = pygame.key.get_pressed()
    
    event = pygame.event.get()
        
    if len(event) != 0 :
        event = event[0]

        if event.type == QUIT :
            run = False

    if not end :

        if keys[pygame.K_RIGHT] :
            mouse0.direction = 'cw'
        elif keys[pygame.K_LEFT] :
            mouse0.direction = 'ccw'
        elif keys[pygame.K_DOWN] :
            mouse0.direction = 'in'
        elif keys[pygame.K_UP] :
            mouse0.direction = 'out'
        else :
            mouse0.direction = 'none'

        if abs(mouse0.θ-cat.θ)%(2*m.pi) < 0.01 :
            cat.direction = 'none'
        elif mouse0.θ > cat.θ :
            cat.direction = 'cw'
        elif mouse0.θ < cat.θ :
            cat.direction = 'ccw'

    if keys[pygame.K_RETURN] :
        end = False
        mouse0.r, mouse0.θ = 5, 0
        cat.r, cat.θ = 200, 0

    mouse0.move()
    cat.move()
    printScreen(surface, mouse0, cat)
    if mouse0.r >= 200 and (cat.θ-mouse0.θ)%(2*m.pi) > 0.01 :
        print('win')
        end = True
        mouse0.direction = 'none'
        cat.direction = 'none'
    elif mouse0.r >= 200 and (cat.θ-mouse0.θ)%(2*m.pi) < 0.01 :
        print('lose')
        end = True
        mouse0.direction = 'none'
        cat.direction = 'none'
        
pygame.quit()
