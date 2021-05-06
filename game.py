import pygame
from player import Player
###création d'une classe jeau 
class Game:
    def __init__(self):
        ###générer le joueur
        self.player = Player()
        self.pressed ={}
