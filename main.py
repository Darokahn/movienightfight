from dataclasses import dataclass
import pygame
import json
import importlib
import types
import sys
import copy
from pathlib import Path

print(__file__)
root_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(root_dir))

JUMPHEIGHT = 20
VELOCITYPRESERVATION = 0.90
GRAVITY = 3
FLOORLINE = 400

def loadScript(playerName):
    spec = importlib.util.spec_from_file_location("temp_module", "players/" + playerName + "/script.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class Player:
    def __init__(self, x, y, health, name, scale):
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.health = health
        self.scale = scale
        self.script = loadScript(name)
        self.currentState = 0
    def jump(self):
        self.velocityY -= JUMPHEIGHT
    def evolve(self):
        self.y += self.velocityY
        self.x += self.velocityX
        self.velocityX *= VELOCITYPRESERVATION
        self.velocityY *= VELOCITYPRESERVATION
        if self.y + self.getHeight() < FLOORLINE:
            self.doGravity()
        else:
            self.y = FLOORLINE - self.getHeight()
    def getSprite(self):
        self.script.sprites[self.currentState].current += 1
        if self.script.sprites[self.currentState].current >= self.script.sprites[self.currentState].frameCount:
            self.script.sprites[self.currentState].current = 0
        return self.script.sprites[self.currentState].getSprite()
    def getHeight(self):
        return self.getMainHitbox().height
    def getWidth(self):
        return self.getMainHitbox().width
    def doGravity(self):
        self.velocityY += GRAVITY
    def getMainHitbox(self):
        hitbox = copy.copy(self.script.hitboxes[self.currentState][0])
        hitbox.x *= self.script.aspectRatio[0]
        hitbox.y *= self.script.aspectRatio[1]
        hitbox.width *= self.script.aspectRatio[0]
        hitbox.height *= self.script.aspectRatio[1]
        hitbox.x += self.x
        hitbox.y += self.y
        print(hitbox.x, hitbox.y, hitbox.width, hitbox.height)
        return hitbox

screen = pygame.display.set_mode((320 * 4, 240 * 4))

p = Player(0, 160, 10, "liam", 1)

stage = pygame.Surface((320, 240))

clock = pygame.time.Clock()

i = 0
while True:
    if i % 60 == 0:
        p.jump()
    i += 1
    pygame.event.get()
    clock.tick(30)
    stage.fill((0, 0, 0))
    screen.fill((0, 0, 0))
    p.evolve()
    screen.blit(p.getSprite(), (p.x, p.y))
    print(p.getMainHitbox().containsPoint(pygame.mouse.get_pos()))
    pygame.display.flip()
