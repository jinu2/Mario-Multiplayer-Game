import pygame
from network import Network
from player import Player

width = 800
height = 800
win = pygame.display.set_mode((width, height))

running = True

img = pygame.image.load("bg.gif")
img.convert()
rect = img.get_rect()
rect.center = width // 2, height // 2
moving = False



pygame.display.set_caption("Client")
#
# catImg = pygame.image.load("cat (1).png")
# dogImg = pygame.image.load("dog.png")


def redrawWindow(win,player, player2):
    win.blit(img, rect)
    player.draw1(win)
    player2.draw1(win)
    pygame.display.flip()



def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()