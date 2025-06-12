from dataclasses import dataclass
import pygame
import json
import importlib
import types

JUMPHEIGHT = 20
VELOCITYPRESERVATION = 0.99

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
        self.currentState = 0
    def jump(self):
        self.velocityY -= JUMPHEIGHT
    def evolve(self):
        self.y += self.velocityY
        self.x += self.velocityX
        self.velocityX *= VELOCITYPRESERVATION
        self.velocityY *= VELOCITYPRESERVATION
    def getSprite(self):
        return self.stateLibrary[self.currentState].sprite

screen = pygame.display.set_mode((320 * 4, 240 * 4))

p = Player(0, 0, 10, "Liam", "")

stage = pygame.Surface((320, 240))

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    stage.fill((0, 0, 0))
    screen.fill((0, 0, 0))
    pygame.display.flip()
