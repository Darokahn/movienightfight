
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

