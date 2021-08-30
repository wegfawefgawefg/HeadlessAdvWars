class Unit:
    def __init__(self,
            unit_type, fuel, ammo, range, movement_type, mp, cost, built_from, vision):
        self.unit_type = unit_type
        self.hp = 100
        self.fuel = fuel
        self.ammo = ammo
        self.range = range
        self.movement_type = movement_type
        self.mp = mp
        self.cost = cost
        self.built_from = built_from
        self.vision = vision

    def take_damage(self, damage):
        self.hp -= damage
        self.hp = max(0.0, self.hp)
