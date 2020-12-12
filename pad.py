import requests
from bs4 import BeautifulSoup


class PuzzlesDragons:
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
        r = requests.get("http://www.puzzledragonx.com/en/monster.asp",
                         params={"n": monster_id})
        print("Page Requested")
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
        r = requests.get("http://www.puzzledragonx.com/en/"+awoken_skill_url)
        print("Page Requested ", r.status_code)
        if 200 <= r.status_code < 300:
            soup = BeautifulSoup(r.text, "html.parser")
            return soup
        else:
            raise Exception(
                f"This Awoken Skills page could not be made: {r.status_code}")

    @staticmethod
    def read_home_page_soup():
        """ Requesting the home page for that pages html

        Raises:
            Exception: status code for request 

        Returns:
            bs4: A Beautiful soup object containing the home pages html
        """
        r = requests.get("http://www.puzzledragonx.com/")
        print("Page Requested ", r.status_code)

        if 200 <= r.status_code < 300:
            soup = BeautifulSoup(r.text, "html.parser")
            return soup
        else:
            raise Exception(
                f"The Home page could not be made: {r.status_code}")

    @staticmethod
    def read_dungeon_page_soup(dungeon_url):
        """ Requesting the dungeon page for that pages html

        Args:
            dungeon_url (str): A url containing the dungeon redirect

        Raises:
            Exception: status code for request 

        Returns:
            bs4: A Beautiful soup object containing the dungeon pages html
        """
        r = requests.get("http://www.puzzledragonx.com/"+dungeon_url)
        print("Page Requested ", r.status_code)
        if 200 <= r.status_code < 300:
            soup = BeautifulSoup(r.text, "html.parser")
            return soup
        else:
            raise Exception(
                f"This Dungeon page could not be made: {r.status_code}")
