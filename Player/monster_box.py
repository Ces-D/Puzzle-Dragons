from os import stat
from monsters import MonsterStats
from pad import UpdatedMonstersContent
import pandas as pd
import os
import sqlite3


class MonsterBox:
    @staticmethod
    def create_monster_box():
        conn = sqlite3.connect("Player/PuzzleDragons.db")
        command = """ CREATE TABLE IF NOT EXISTS monster_box
            (monster_id text,
            name text,
            type_ text,
            element text,
            rarity text,
            cost integer,
            monster_points integer,
            limit_break text,
            skills_active_skill text,
            skills_active_skill_effect text,
            skills_active_skill_cooldown text,
            skills_assist integer,
            skills_leader_skill text,
            skills_leader_skill_effect text,
            skills_awakenings text,
            skills_super_awakenings text)"""
        c = conn.cursor()
        c.execute(command)
        conn.commit()
        conn.close()

    @ staticmethod
    def add(monster_id):
        conn = sqlite3.connect("Player/PuzzleDragons.db")
        monster_profile = MonsterStats.monster_profile(
            monster_id=monster_id)
        command = """
        INSERT into monster_box VALUES
        (:monster_id,
        :name,
        :type_,
        :element,
        :rarity,
        :cost,
        :monster_points,
        :limit_break,
        :skills_active_skill,
        :skills_active_skill_effect,
        :skills_active_skill_cooldown,
        :skills_assist in,
        :skills_leader_skill,
        :skills_leader_skill_effect,
        :skills_awakenings,
        :skills_super_awakenings)
        """
        c = conn.cursor()
        c.execute(command)
        conn.commit()
        conn.close()
# TODO: convert the dict response from MOnsterStats.monster_profile into tuple

    @ staticmethod
    def remove(monster_id):
        # remove a monster from monster box aka monster_box.csv
        pass

    @ staticmethod
    def check_for_updates():
        # check the recently updated cards for any cards in players monster box
        pass


# TODO: convert to sqlite. create DB class to be inherited by MonsterBox class
