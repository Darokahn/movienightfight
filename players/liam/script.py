import pygame
import sys
from pathlib import Path


import playerUtils as pu

states = [
    {
        "hitboxes": [
            [0, 0, 1, 1, 0, ""],
        ],
        "hurtboxes": [
            [0, 0, 2, 1]
        ],
        "appearance": {
            "path": "liam.png",
            "frameDimensions": [64, 80],
            "frameCount": 4,
            "frameRate": 2
        }
    },
]

name = "liam"

aspectRatio = [64, 80]

basePath = "players/liam/sprites/"

sprites = []
hitboxes = []

for state in states:
    sprites.append(
            pu.AnimatedSprite(basePath + state["appearance"]["path"], state["appearance"]["frameDimensions"], state["appearance"]["frameCount"])
            )
    newHitboxes = []
    for hitbox in state["hitboxes"]:
        newHitboxes.append(pu.Hitbox(*hitbox))
    hitboxes.append(newHitboxes)
