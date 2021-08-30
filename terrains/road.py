import core
class Road(core.Terrain):
    def __init__(self) -> None:
        super().__init__(
            terrain_type="road",
            stars=0)
