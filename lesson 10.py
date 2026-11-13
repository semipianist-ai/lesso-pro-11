import pygame
import sys
import time

pygame.init()
clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Flap Bird")

run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    ground_scroll = 0
    scroll_speed = 4

    bg = pygame.image.load('backg.png')
    ground_img = pygame.image.load('ground.jpg')

    screen.blit(bg, (0,0))
    screen.blit(ground_img,(ground_scroll, 768))

class Bird(pygame.sprite.Sprite):
    def _init_(self,x,y):
        super()._init_()
        self.images = [pygame.images.load(f"bird(i).png") for i in range(1 ,4)]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        self.vel + = 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.y + = int(self.vel)

pygame.quit()