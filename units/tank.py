import core
class Tank(core.Unit):
    def __init__(self) -> None:
        super().__init__(
            unit_type="tank",
            fuel=70, 
            ammo=9, 
            range=1, 
            movement_type="treads", 
            mp=6, 
            cost=7000, 
            built_from="factory", 
            vision=3)
