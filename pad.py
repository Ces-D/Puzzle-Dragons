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
        if 200 <= r.status_code < 300:
            soup = BeautifulSoup(r.text, "html.parser")
            return soup
        else:
            raise Exception(
                f"The Home page could not be made: {r.status_code}")


class Content:
    def __init__(self, page):
        self.page = page


class MonsterContent(Content):
    def __init__(self, page):
        Content.__init__(self, page)
        self.monster_page = page

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

    def abilities(self):
        """ Unique class name for a monsters abilities

        Returns:
            List: A list of bs4 objects containing a monsters abilities
        """
        abilities = self.content_stats()[3]
        return abilities.find_all(class_="value-end")


class AwokenSkillsContent(Content):
    def __init__(self, page):
        Content.__init__(self, page)
        self.awoken_page = page

    def monster_awoken_abilities(self):
        """Both Awoken and Super Awoken abilities

        Returns:
            List: containing awoken and super awoken skills specific to a monster
        """
        skills = self.content_stats()[3]
        return skills.find_all(class_="awoken1")

    def monster_awakenings_links(self):
        try:
            awakenings_list = self.monster_awoken_abilities()[0]
            awakenings_a = awakenings_list.find_all("a")
            awakenings = [skill.get("href")
                          for skill in awakenings_a]
        except IndexError:
            return ""
        return awakenings

    def monster_super_awakenings_links(self):
        try:
            s_awakenings_list = self.monster_awoken_abilities()[1]
            s_awakenings_a = s_awakenings_list.find_all("a")
            super_awakenings = [super_skill.get(
                "href") for super_skill in s_awakenings_a]
        except IndexError:
            return ""
        return super_awakenings

    @staticmethod
    def awakening_description(awoken_skill_url):

        skill_soup = PuzzlesDragons.read_awoken_skill_soup(
            awoken_skill_url=awoken_skill_url)
        description = skill_soup.find(class_="nowrap").get_text()
        return description


class UpdatedMonstersContent(Content):
    def __init__(self, page):
        Content.__init__(self, page)
        self.home_page = page

    def get_updated_table(self):
        tab1 = self.home_page.find(id="tab1")
        table = tab1.find_all(id="event")[6]
        return table #should return the correct table

        #TODO: consider shortening the classes for MonsterContent and AwokenSkillsContent into something like this
        ## one method that returns what you are looking for

