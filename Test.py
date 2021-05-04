import pygame
pygame.init()


######Générer la fenêtre du jeu"""#######
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/bg.jpg ")

running = True

#####boucle tant que cette condition est vrai ###
while running:
    ###appliquer l'arrière plan du jeu###
    screen.blit(background,(0,-200))
    ##mettre à jour l'écran 
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            pygame.quit()

