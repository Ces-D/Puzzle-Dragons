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

    def content_profile(self):
        content = self.get_monster_content()
        profile = content.find_all(id="tableprofile")
        return profile

    def monster_profile(self):
        content_profile = self.content_profile()
        profile = Profile(profile=content_profile)
        monster_profile = {"name": profile.name(), "type": profile.type_()}
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
        pass

    def rarity(self):
        pass

    def cost(self):
        pass

    def monster_points(self):
        pass

    def limit_break(self): pass
