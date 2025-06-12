from dataclasses import dataclass
import pygame
import json

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

class State:
    def __init__(self, hitboxes, hurtboxes, spritepath):
        self.hitboxes = hitboxes
        self.hurtboxes = hurtboxes
        self.spritepath = spritepath
        self.sprite = pygame.image.load(spritepath)
    @classmethod
    def fromFile(cls, path):
        data = None
        with open(path, "r") as file:
            data = json.loads(file.read())
        for i in range(len(data["hitboxes"])):
            data["hitboxes"][i] = Hitbox(*data["hitboxes"][i])
        for i in range(len(data["hurtboxes"])):
            data["hurtboxes"][i] = Hurtbox(*data["hurtboxes"][i])
        return cls(**data)

@dataclass
class Player:
    x: int
    y: int
    health: int
    events: dict
    stateLibrary: list
    scriptLibrary: dict
    currentState: int
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
