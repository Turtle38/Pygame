import pygame
pygame.init()

##creation de la class joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

######Générer la fenêtre du jeu"""#######
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))
###importer background######
background = pygame.image.load("assets/bg.jpg ")

####charger notre joueur###
player = Player()


running = True

#####boucle tant que cette condition est vrai ###
while running:
    ###appliquer l'arrière plan du jeu###
    screen.blit(background,(0,-200))

    ###appliquer l'image du joueur###
    screen.blit(player.image,player.rect)

    ##mettre à jour l'écran 
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
            pygame.quit()

