from dataclasses import dataclass
import pygame
import json
import importlib
import types

JUMPHEIGHT = 20
VELOCITYPRESERVATION = 0.90
GRAVITY = 1

def loadScript(playerName):
    spec = importlib.util.spec_from_file_location("temp_module", "players/" + playerName + "/script.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
 

class Hitbox:
    def __init__(self, x, y, width, height, damage, call):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage
        self.call = call

class Hurtbox:
    def __init__(self, x, y, width, height, vulnerability):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vulnerability = vulnerability

class Player:
    def __init__(self, x, y, health, name, libraryPath):
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.health = health
        self.name = name
        self.libraryPath = libraryPath
        self.library = loadScript(name)
        self.currentState = 0
    def jump(self):
        self.velocityY -= JUMPHEIGHT
    def evolve(self):
        print("hello")
        self.y += self.velocityY
        self.x += self.velocityX
        self.velocityX *= VELOCITYPRESERVATION
        self.velocityY *= VELOCITYPRESERVATION
        self.doGravity()
    def getSprite(self):
        return self.library.sprites[self.currentState]
    def doGravity(self):
        self.velocityY += GRAVITY

screen = pygame.display.set_mode((320 * 4, 240 * 4))

p = Player(0, 160, 10, "liam", "")

stage = pygame.Surface((320, 240))

clock = pygame.time.Clock()

p.jump()

while True:
    pygame.event.get()
    clock.tick(30)
    stage.fill((0, 0, 0))
    screen.fill((0, 0, 0))
    p.evolve()
    screen.blit(p.getSprite(), (p.x, p.y))
    pygame.display.flip()
