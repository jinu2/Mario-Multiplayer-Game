import pygame

class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        IMAGE = pygame.image.load("mario.png")
        self.rect = IMAGE.get_rect()
        self.vel = 3
        self.score = 0

    def draw1(self, win):
        IMAGE = pygame.image.load("mario.png")  # or .convert_alpha()
        # Create a rect with the size of the image.
        rect = IMAGE.get_rect()
        rect.center = (self.x, self.y)
        win.blit(IMAGE,rect)

        # pygame.draw.rect(win, self.color, self.rect)

     def draw2(self,win):
         IMAGE = pygame.image.load("luigi.png")  # or .convert_alpha()
    # #     # Create a rect with the size of the image.
         IMAGE = pygame.transform.scale(IMAGE, (40,59))
         rect = IMAGE.get_rect()
         rect.center = (self.x, self.y)
         win.blit(IMAGE, rect)
         # pygame.draw.rect(win, self.color, self.rect)


    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if(self.x>0):
                self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            if (self.x < 750):
                self.x += self.vel

        if keys[pygame.K_UP]:
            if (self.y >0):
                self.y -= self.vel

        if keys[pygame.K_DOWN]:
            if (self.y < 750):
                self.y += self.vel

        self.update()

    def update(self):
        self.rect  = (self.x, self.y)
        if self.y < 40:
            self.y = 700
            self.score += 1


