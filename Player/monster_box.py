from typing import final
from monsters import MonsterStats
from pad import PuzzlesDragons, UpdatedMonstersContent
from sqlite3.dbapi2 import IntegrityError, paramstyle
import sqlite3


class MonsterBox:
    @staticmethod
    def create_monster_box():
        conn = sqlite3.connect("Player/PuzzleDragons.db")
        command = """ CREATE TABLE IF NOT EXISTS monster_box
            (monster_id TEXT UNIQUE,
            name TEXT,
            type_ TEXT,
            element TEXT,
            rarity TEXT,
            cost INTEGER,
            monster_points INTEGER,
            limit_break TEXT,
            active_skill TEXT,
            active_skill_effect TEXT,
            active_skill_cooldown TEXT,
            assist_status TEXT,
            leader_skill TEXT,
            leader_skill_effect TEXT,
            awakenings TEXT,
            super_awakenings TEXT)"""
        c = conn.cursor()
        c.execute(command)
        conn.commit()
        conn.close()

    @ staticmethod
    def add(monster_id):
        conn = sqlite3.connect("Player/PuzzleDragons.db")
        try:
            monster_profile = MonsterStats.monster_profile(monster_id)
            sql_ = """
            INSERT INTO monster_box VALUES
            (:monster_id,
            :name,
            :type_,
            :element,
            :rarity,
            :cost,
            :monster_points,
            :limit_break,
            :active_skill,
            :active_skill_effect,
            :active_skill_cooldown,
            :assist_status,
            :leader_skill,
            :leader_skill_effect,
            :awakenings,
            :super_awakenings)
            """
            c = conn.cursor()
            c.execute(sql_, monster_profile)
            conn.commit()
            print(f"Monster ID: {monster_id} ADDED")
        except IntegrityError:
            print("Monster ID must be UNIQUE")
        conn.close()

    @ staticmethod
    def remove(monster_id):
        conn = sqlite3.connect("Player/PuzzleDragons.db")
        c = conn.cursor()
        c.execute("DELETE FROM monster_box WHERE monster_id=?", (monster_id,))
        conn.commit()
        conn.close()
        print(f"Monster ID: {monster_id} REMOVED")

    @ staticmethod
    def check_for_updates():
        conn = sqlite3.connect("Player/PuzzleDragons.db")
        try:
            updated_content = UpdatedMonstersContent(
                PuzzlesDragons.read_home_page_soup())
            updated_ids = updated_content.updated_monster_ids()
            for monster_id in updated_ids:
                c = conn.cursor()
                c.execute(
                    "SELECT * FROM monster_box WHERE monster_id=?", (monster_id,))
                monster_exists = c.fetchone()
                if monster_exists:
                    sql_ = """
                    UPDATE OR ABORT monster_box
                    SET 
                    name = :name, 
                    type_ = :type_, 
                    element = :element, 
                    rarity = :rarity, 
                    cost = :cost, 
                    monster_points = :monster_points,
                    limit_break = :limit_break, 
                    active_skill = :active_skill, 
                    active_skill_effect = :active_skill_effect,
                    active_skill_cooldown = :active_skill_cooldown, 
                    assist_status = :assist_status,
                    leader_skill = :leader_skill, 
                    leader_skill_effect = :leader_skill_effect,
                    awakenings = :awakenings,
                    super_awakenings = :super_awakenings
                    WHERE monster_id = :monster_id
                    """
                    params = MonsterStats.monster_profile(monster_id)
                    c.execute(sql_, params)
            conn.commit()
        except sqlite3.Error as error:
            print("Failed to update table: ", error)
        conn.close()

    @staticmethod
    def list_monster_box():
        conn = sqlite3.connect("Player/PuzzleDragons.db")
        c = conn.cursor()
        c.execute("SELECT monster_id FROM monster_box")
        print(c.fetchall())
        conn.close()
