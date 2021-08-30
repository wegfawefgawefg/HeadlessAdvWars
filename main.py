class Game:
    pass
class Map:
    pass

import json
with open("damage_chart.json", "r") as f:
    DAMAGE_CHART = json.load(f)

def calc_damage(attacking_unit, defending_unit, attacking_co, defending_co, defending_terrain):
    '''https://awbw.fandom.com/wiki/Damage_Formula'''
    base_damage = DAMAGE_CHART[attacking_unit.unit_type][defending_unit.unit_type]
    defending_terrain.defense_rating = 1
    damage = (
        (base_damage * attacking_co.attack / 100.0) * 
        ((attacking_unit.hp / 10.0) / 10.0) * (
            (200.0 - (defending_co.defense + defending_terrain.defense_rating * 
                (defending_unit.hp / 10.0))) 
            / 100.0))
    return damage

def damage_test():
    import units
    import cos
    import terrains

    atk_co = cos.Bland()
    atk_unit = units.Tank()
    atk_terrain = terrains.Road()

    def_co = cos.Bland()
    def_unit = units.Tank()
    def_terrain = terrains.Road()

    dmg = calc_damage(atk_unit, def_unit, atk_co, def_co)
    def_unit.take_damage(dmg)
    counter_dmg = calc_damage(def_unit, atk_unit, def_co, atk_co)
    print(f"dmg {dmg}")
    print(f"cntr_dmg {counter_dmg}")

damage_test()