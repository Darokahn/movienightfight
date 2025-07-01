import pygame

class Hitbox:
    def __init__(self, x, y, width, height, damage, call):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.damage = damage
        self.call = call
    def containsPoint(self, point):
        if ((point[0] > self.x and point[0] < self.x + self.width) and 
            (point[1] > self.y and point[1] < self.y + self.height)):
            return True
        return False

class Hurtbox:
    def __init__(self, x, y, width, height, vulnerability):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vulnerability = vulnerability
    def containsPoint(self, point):
        if ((point[0] > self.x and point[0] < self.x + self.width) and 
            (point[1] > self.y and point[1] < self.y + self.height)):
            return True
        return False

class AnimatedSprite:
    def __init__(self, path, frameResolution, frameCount):
        self.path = path
        self.frameResolution = frameResolution
        self.frameCount = frameCount

        self.masterSprite = pygame.image.load(path)
        self.subSprites = []
        for i in range(frameCount):
            newSprite = pygame.Surface(frameResolution)
            newSprite.blit(self.masterSprite, (-i * frameResolution[0], 0))
            self.subSprites.append(newSprite)
        self.current = 0
    def getSprite(self):
        return self.subSprites[self.current]
