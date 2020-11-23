import requests
from bs4 import BeautifulSoup


class PuzzlesDragons:
    MONSTER_URL = "http://www.puzzledragonx.com/en/monster.asp"

    @staticmethod
    def read_monster_soup(monster_id):
        """ Requesting a monsters page for the pages html

        Args:
            monster_id (str): A monsters id 

        Raises:
            Exception: status code for request

        Returns:
            [bs4] :  A Beautiful soup object containing the specific monsters html
        """
        r = requests.get(PuzzlesDragons.MONSTER_URL,
                         params={"n": monster_id})
        if 200 <= r.status_code < 300:
            soup = BeautifulSoup(r.text, "html.parser")
            return soup
        else:
            raise Exception(
                f"Monster request could not be made: {r.status_code}")

    @staticmethod
    def read_awoken_skill_soup(awoken_skill_url):
        """ Requesting an awoken skills page for that pages html

        Args:
            awoken_skill_url (str): A url containing params for the awoken skill

        Raises:
            Exception: status code for request

        Returns:
            [bs4]: a Beautiful soup object containing the awoken skills page html
        """
        r = requests.get(awoken_skill_url)
        if 200 <= r.status_code < 300:
            soup = BeautifulSoup(r.text, "html.parser")
            return soup
        else:
            raise Exception("This Awoken Skills page could not be made")


class Content:
    def __init__(self, monster_page, awoken_skills_page):
        self.monster_page = monster_page
        self.awoken_skills_page = awoken_skills_page