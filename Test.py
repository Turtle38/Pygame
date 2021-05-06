import pygame
from game import Game
from player import Player
pygame.init()





######Générer la fenêtre du jeu"""#######
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))
###importer background######
background = pygame.image.load("assets/bg.jpg ")

###Charger le jeu
game = Game()



running = True

#####boucle tant que cette condition est vrai ###
while running:
    ###appliquer l'arrière plan du jeu###
    screen.blit(background,(0,-200))

    ###appliquer l'image du joueur###
    screen.blit(game.player.image,game.player.rect)
    ##vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()


    
    ##mettre à jour l'écran 
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            pygame.quit()
    ###détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        
            
        

