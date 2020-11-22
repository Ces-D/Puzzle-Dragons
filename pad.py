import requests
from bs4 import BeautifulSoup
from monster_skills import AwokenSkills, Skills
from monster_profile import Profile


class PuzzlesDragons:
    MONSTER_URL = "http://www.puzzledragonx.com/en/monster.asp"

    def __init__(self):
        pass

    def request_monster_page(self, monster_id):
        """ Request the monsters url for a specific monster page

        Args:
            monster_id ([str]): [A monster id]
        """
        r = requests.get(PuzzlesDragons.MONSTER_URL,
                         params={"n": monster_id})
        if 200 <= r.status_code < 300:
            return r.text
        else:
            raise Exception(
                f"Monster request could not be made: {r.status_code}")

    def read_monster_soup(self, page):
        """ Return the text file of the HTML page previously requested

        Args:
            page ([text]): [Response text of a request]
        """
        soup = BeautifulSoup(page, "html.parser")
        return soup


class MonsterStats:
    def __init__(self, monster_page):
        """ Returns all relevent statistics for a specific game monster

        Args:
            monster_page (BeautifulSoup): A Beautiful soup object containing monster request
        """
        self.monster_page = monster_page

    def get_monster_content(self):
        """
        Returns:
            bs4: Content containing monster info
        """
        content = self.monster_page.find(id="content")
        return content

    def content_stats(self):
        """ Accessing generic-ly named id for tables of monster info

        Returns:
            List: A list of Beautiful soup objects containing monster info
        """
        content = self.get_monster_content()
        content_stats = content.find_all(id="tablestat")
        return content_stats

    def content_profile(self):
        """ Access uniquely named id for getting monster profile

        Returns:
            List: A list of Beautiful soup objects containing basic monster profile
        """
        content = self.get_monster_content()
        profile = content.find_all(id="tableprofile")
        return profile

    def monster_profile(self):
        profile = Profile(profile=self.content_profile())
        skills = Skills(contents=self.content_stats())
        monster_profile = {
            "name": profile.name(),
            "type": profile.type_(),
            "element": profile.element(),
            "rarity": profile.rarity(),
            "cost": profile.cost(),
            "monster_points": profile.monster_points(),
            "limit_break": profile.limit_break(),
            "skills": [
                {
                    "active_skill": skills.active_skill_name(),
                    "active_skill_effect": skills.active_skill_effect(),
                    "active_skill_cooldown": skills.active_skill_cooldown()
                },
                {
                    "assist": skills.assist_status()
                },
                {
                    "leader_skill": skills.leader_skill_name(),
                    "leader_skill_effect": skills.leader_skill_effect(),
                },
                {
                    "awakenings": skills.monster_awakenings_links(),
                    "super_awakenings": skills.monster_super_awakenings_links()
                }
            ]
        }
        return monster_profile
