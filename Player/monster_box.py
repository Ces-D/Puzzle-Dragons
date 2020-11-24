from monsters import MonsterStats
from pad import UpdatedMonstersContent
import pandas as pd
import os
import csv


class MonsterBox:

    @staticmethod
    def create_monster_box():
        if os.path.isfile("Player/Monster-Box.csv"):
            print("Monster Box exists")
            pass
        else:
            headers = ["id", "name", "type",
                       "element", "rarity",
                       "cost", "monster_points",  "limit_break",
                       "skills.active_skill", "skills.active_skill_effect",
                       "skills.active_skill_cooldown",
                       "skills.assist", "skills.leader_skill",
                       "skills.leader_skill_effect",
                       "skills.awakenings", "skills.super_awakenings", ]
            with open("Player/Monster-Box.csv", "w") as monster_box:
                writer = csv.writer(monster_box)
                writer.writerow(headers)

    @ staticmethod
    def add(monster_id):
        # the monster profile plus stats are added to a specific csv file
        pass

    @ staticmethod
    def remove(monster_id):
        # remove a monster from monster box aka monster_box.csv
        pass

    @ staticmethod
    def check_for_updates():
        # check the recently updated cards for any cards in players monster box
        pass
