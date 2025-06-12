import pygame

states = [
    {
        "hitboxes": [
            [0, 0, 2, 2],
        ],
        "hurtboxes": [
            [0, 0, 2, 1]
        ],
        "appearance": {
            "path": "liam.png",
            "frameDimensions": [0, 0],
            "frameCount": 0,
            "frameRate": 0
        }
    },
]

sprites = []

for state in states:
    sprites.append(
            pygame.image.load("players/liam/sprites/" + state["appearance"]["path"])
            )
