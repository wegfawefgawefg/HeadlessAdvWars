class Game:
    pass
class Map:
    pass

import json
with open("damage_chart.json", "r") as f:
    DAMAGE_CHART = json.load(f)

def calc_damage(attacker, defender):
    '''https://awbw.fandom.com/wiki/Damage_Formula'''
    base_damage = DAMAGE_CHART[attacker.unit_type][defender.unit_type]
    tile_rating = 1
    co_attack = 100
    co_defense = 100
    damage = (
        (base_damage * co_attack / 100.0) * 
        ((attacker.hp / 10.0) / 10.0) * (
            (200.0 - (co_defense + tile_rating * (defender.hp / 10.0))) / 
                100.0))
    return damage

def damage_test():
    import units
    atk_unit = units.Tank()
    dfnd_unit = units.Tank()
    dmg = calc_damage(atk_unit, dfnd_unit)
    dfnd_unit.take_damage(dmg)
    counter_dmg = calc_damage(dfnd_unit, atk_unit)
    print(f"dmg {dmg}")
    print(f"cntr_dmg {counter_dmg}")