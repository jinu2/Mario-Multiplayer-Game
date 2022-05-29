import pygame
from network import Network

pygame.init()
pygame.font.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))

running = True

img = pygame.image.load("bg.gif")
img.convert()
rect = img.get_rect()
rect.center = width // 2, height // 2
moving = False
level = 1

pygame.display.set_caption("Client")


# catImg = pygame.image.load("cat (1).png").convert()
# dogImg = pygame.image.load("dog.png").convert()


def redrawWindow(win, player, player2):
    win.blit(img, rect)
    player.draw1(win)
    player2.draw2(win)

    font_colour = (0, 0, 0)
    if player.score == 3:
        fontx = pygame.font.Font(None, 100)
        textx = fontx.render("Player 1 Wins", True, (255, 0, 0))
        win.blit(textx, (200, 200))
    elif player2.score == 3:
        fontx = pygame.font.Font(None, 100)
        textx = fontx.render("Player 2 Wins", True, (255, 0, 0))
        win.blit(textx, (200, 200))

    font1 = pygame.font.Font(None, 50)
    text1 = font1.render(str(player.score), True, font_colour)
    font2 = pygame.font.Font(None, 50)
    text2 = font2.render(str(player2.score), True, font_colour)
    win.blit(text1, (150, 50))
    win.blit(text2, (650, 50))
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
                pygame.quit()
                run = False

        p.move()
        redrawWindow(win, p, p2)


main()
