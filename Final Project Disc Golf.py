# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:09:25 2023

@author: manof
person - https://opengameart.org/content/person-retail-employee
disc - https://opengameart.org/content/glow-circle

"""
import simpleGE
import pygame

class person (simpleGE.BasicSprite):
    def __init__(self, scene):
        super(). __init__(scene)
        self.setImage ("discPerson.png")
        self.setSize (30,30)
        self.y = (400)
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.turnBy(5)
        elif self.scene.isKeyPressed(pygame.K_RIGHT):
            self.turnBy(-5)
        
class game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.person = person(self)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (50,30)
        self.score = 0
        
        self.lblHole = simpleGE.Label()
        self.lblHole.text = "Hole #1"
        self.lblHole.center = (550,30)
class Disc(simpleGE.SuperSprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("glowCircle.png")
        self.setBoundAction(self.HIDE)
        self.hide()
        
        def throw(self):
            self.show()
            self.setPosition(self.parent.rect.center)
        
        
def main():
    game = simpleGE.Scene()
    game.background.fill("papayawhip")
    game.person = person(game)
    game.sprites = [game.person]
    game.start()
    
if __name__ == "__main__":
    main()