# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:09:25 2023

@author: manof
person - https://opengameart.org/content/person-retail-employee
disc - https://opengameart.org/content/glow-circle
reticle - https://opengameart.org/content/high-resolution-crosshairs
"""
import simpleGE
import pygame
import math

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
    
class Crosshair(simpleGE.BasicSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("cross.png")
        self.setSize(50,50)
        
    def checkEvents(self):
        (mx, my) = pygame.mouse.get_pos()
        self.x = mx
        self.y = my
        
class Scene1(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.next = ""
        self.lblOutput = simpleGE.Label()
        self.lblOutput.center = ((320, 240))
        self.lblOutput.size = ((300, 30))
        self.lblOutput.text = "Hole #1"
        
        self.btn2 = simpleGE.Button()
        self.btn2.center = ((220,340))
        self.btn2.text = "Go to Hole 2"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = ((420, 340))
        self.btnQuit.text = "Quit"
        
        self.sprites = [self.lblOutput, self.btn2, self.btnQuit]
    def update(self):
        if self.btn2.clicked:
            self.next = "2"
            self.stop()
            
        if self.btnQuit.clicked:
            self.stop()
            
class Scene2(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.lblOutput = simpleGE.Label()
        
        self.lblOutput.center = ((320, 240))
        self.lblOutput.size = ((300, 30))
        self.lblOutput.text = "Hole 2"
        
        self.btn3 = simpleGE.Button()
        self.btn3.center = ((220,340))
        self.btn3.text = "Go to Hole 3"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = ((320,340))
        self.btnQuit.text = "Quit"
        
    def update(self):
        if self.btnQuit.clicked:
            self.stop()
            
class Scene3(simpleGE.Scene):
    def __init__(self):
        self.lblOutput = simpleGE.Label()
        self.lbnlOutput.center = (320,240)
        self.lblOutput.text = "Hole 3"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = ((320, 340))
        self.btnQuit.text = "Quit"
        
        self.sprites = [self.lblOutput, self.btnQuit]
        
        def update(self):
            if self.btnQuit.clicked:
                self.stop
                

    
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.background.fill(pygame.Color("papayawhip"))
        pygame.mouse.set_visible(False)
        pygame.mixer.music.load("disc golf song.mp3")
        self.currentDisc = 0
        self.NUM_DISCS = 1
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Score: 0"
        self.lblScore.center = (50,30)
        self.score = 0
        
        self.lblHole = simpleGE.Label()
        self.lblHole.text = "Hole #1"
        self.lblHole.center = (550,30)
        
        
        self.person = Person(self)
        self.basket = Basket(self)
        self.crosshair = Crosshair(self)
        self.currentDisc = Disc(self, self.person)
        
        

        #for i in range(self.NUM_DISCS):
            #self.disc.append(Disc(self, self.person))
        self.sprites = [self.lblScore, self.lblHole, self.person, self.basket, self.currentDisc, self.crosshair]
            
    
    def update(self):
        mousePos = pygame.mouse.get_pos()
        power = pygame.mouse.get_rel()
        dist = self.currentDisc.distanceTo(mousePos)
        
        
        
    
class Disc(simpleGE.SuperSprite):
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        self.setImage("glowCircle.png")
        self.imageMaster = pygame.Surface((5,5))
        self.setBoundAction(self.HIDE)
        self.hide()
        
        
    def throw(self):
        self.show()
        self.setPosition(self.parent.rect.center)
        #self.setMoveAngle(self.parent.rotation)
        self.setSpeed(self.scene.scrVelocity.value)
        self.calcVector()
        
    def checkEvents(self):
        if self.visible:
            self.addDY(1)
        else:
            self.setSpeed(0)
            
        
            
    def calcVector(self):
        theta = self.dir / 180.0 * math.pi
        self.dx = math.cos(theta) * self.speed
        self.dy = math.sin(theta) * self.speed
        self.dy *= -1
        
def main():
    game = Game()
    game.start()
    pygame.mouse.set_visible(True)
    
    scene2 = Scene2()
    scene2.start()
    
    scene1 = Scene1()
    scene1.start()

    next = scene1.next
    
    if next == "2":
        scene2 = Scene2()
        scene2.start()
    if next == "3":
        scene3 = Scene3()
        scene3.start()
    
if __name__ == "__main__":
    main()
