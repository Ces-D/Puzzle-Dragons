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
        # 13 and 14 tables
        updated_table = self.home_page.find_all(
            'table')[14]  # Table for updated monsters
        return updated_table

    def updated_monster_ids(self):
        updates = self.get_updated_table()
        update_a_links = updates.find_all("a")
        update_refs = [update_link.get("href") for update_link in update_a_links]
        updated_monster_ids = [monster.split("=")[1] for monster in update_refs]
        return updated_monster_ids


class DungeonContent(Content):
    def __init__(self, page):
        Content.__init__(self, page)
        self.home_page = page

    def get_dungeon_tables(self):
        tabs = self.home_page.find_all("div", attrs={"style":"display: none;"})
        # tab1 = main.find("div", id="tab1")        
        # tab2 = main.find("div", id="tab2")
        # tab3 = main.find("div", id="tab3")
        # tab4 = main.find("div", id="tab4")
        # tab5 = main.find("div", id="tab5")
        # tab6 = main.find("div", id="tab6")
        # tab7 = main.find("div", id="tab7")
        # tab8 = main.find("div", id="tab8")
        return tabs[1] # returns the tabs from 1-8. Tabs 2-8 are what we want
    
    @staticmethod
    def tab_dungeon_refs(tab):
        cols = tab.find_all(class_="column")
        return cols

    # def dungeon_pages(self):
    #     tabs = self.get_dungeon_tables()
    #     dungeon_pages = []  #[{name:ref}]
    #     for tab in tabs:
    #         cols = DungeonContent.tab_dungeon_refs(tab)
    #         dungeon_pages.append(cols)

    #     return dungeon_pages