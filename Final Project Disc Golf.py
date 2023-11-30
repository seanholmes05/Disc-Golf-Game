# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:09:25 2023

@author: manof
person - https://opengameart.org/content/person-retail-employee
disc - https://opengameart.org/content/glow-circle

"""
import simpleGE
import pygame

class Person (simpleGE.BasicSprite):
    def __init__(self, scene):
        super(). __init__(scene)
        self.setImage ("discPerson.png")
        self.setSize (30,30)
        self.y = (400)
        
class Basket(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("basket.png")
        self.setSize(40,40)
        self.y = (200)
        self.x = (500)

    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.background.fill(pygame.Color("papayawhip"))
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (50,30)
        self.score = 0
        
        self.lblHole = simpleGE.Label()
        self.lblHole.text = "Hole #1"
        self.lblHole.center = (550,30)
        
        self.person = Person(self)
        self.basket = Basket(self)
        self.disc = Disc(self)
        
        self.sprites = [self.lblScore, self.lblHole, self.person, self.basket, self.disc]
        

        
class Disc(simpleGE.SuperSprite):
    def __init__(self, scene,):
        super().__init__(scene)
        self.setImage("glowCircle.png")
        self.setBoundAction(self.HIDE)
        self.hide()
        
        def throw(self):
            self.show()
            self.setPosition(self.parent.rect.center)
    
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()
