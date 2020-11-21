import requests
from bs4 import BeautifulSoup


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
                }
            ]
        }
        return monster_profile


class Profile:
    def __init__(self, profile):
        self.profile = profile

    def name(self):
        names = self.profile[0].find_all(class_="data")
        return names[0].get_text()

    def measurements(self):
        measurements = self.profile[1].find_all(class_="data")
        return measurements

    def type_(self):
        measurements = self.measurements()
        type_ = measurements[0].get_text()
        return type_

    def element(self):
        measurements = self.measurements()
        element = measurements[1].get_text()
        return element

    def rarity(self):
        measurements = self.measurements()
        rarity = measurements[2].get_text()
        return rarity

    def cost(self):
        measurements = self.measurements()
        cost = measurements[3].get_text()
        return cost

    def monster_points(self):
        measurements = self.measurements()
        monster_points = measurements[4].get_text()
        return monster_points

    def limit_break(self):
        measurements = self.measurements()
        limit_break = measurements[5].get_text()
        # format response
        return limit_break.split("\r\n\t\t\t\t\t\t\t\t\t\t\t")[1]


class AwokenSkills:
    def __init__(self, contents):
        self.contents = contents

    def abilities(self):
        abilities = self.contents[3]
        return abilities.find_all(class_="value-end")

    


class Skills(AwokenSkills):
    def __init__(self, contents):
        AwokenSkills.__init__(self, contents)
        self.contents = contents

    def active_skill_name(self):
        return self.abilities()[0].get_text()

    def active_skill_effect(self):
        return self.abilities()[1].get_text()

    def active_skill_cooldown(self):
        return self.abilities()[2].get_text()

    def assist_status(self):
        assist_text = self.abilities()[3].get_text()
        if assist_text == "This card can be used as assist.":
            return "True"
        else:
            # return assist_text+"   " + "False"
            return "False"

    def leader_skill_name(self):
        return self.abilities()[4].get_text()

    def leader_skill_effect(self):
        return self.abilities()[5].get_text()

    def awoken_skills(self):
        pass

    def super_awoken_skills(self):
        pass
