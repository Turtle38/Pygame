import pygame
pygame.init()


######Générer la fenêtre du jeu"""#######
pygame.display.set_caption("Comet fall game")
pygame.display.set_mode((1080,720))

running = True

#####boucle tant que cette condition est vrai ###
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            pygame.quit()
