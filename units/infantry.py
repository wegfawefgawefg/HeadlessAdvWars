import core
class Infantry(core.Unit):
    def __init__(self) -> None:
        super().__init__(
            unit_type="infantry",
            fuel=100, 
            ammo=100, 
            range=1, 
            movement_type="legs", 
            mp=3, 
            cost=1000, 
            built_from="factory", 
            vision=5)
