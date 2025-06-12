from dataclasses import dataclass
import pygame
import json
import importlib
import types

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
        self.health = health
        self.name = name
        self.libraryPath = libraryPath
        self.currentState = 0
    def getSprite(self):
        return self.stateLibrary[self.currentState].sprite

screen = pygame.display.set_mode((320 * 4, 240 * 4))

s1 = State.fromFile("liam.json")

p = Player(0, 0, 100, {}, [s1], {}, 0)

stage = pygame.Surface((320, 240))

while True:
    stage.fill((0, 0, 0))
    screen.fill((0, 0, 0))
    screen.blit(p.getSprite(), (0, 0))
    pygame.display.flip()
