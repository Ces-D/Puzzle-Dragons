from pad import PuzzlesDragons

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
        update_refs = [update_link.get("href")
                       for update_link in update_a_links]
        updated_monster_ids = [monster.split(
            "=")[1] for monster in update_refs]
        return updated_monster_ids


class DungeonContent(Content):
    def __init__(self, page):
        Content.__init__(self, page)
        self.home_page = page

    def dungeon_names(self):
        dungeons_list = self.home_page.find_all(class_="dungeonname")
        dungeons = [(dungeon.get_text(), dungeon.a.get("href"))
                    for dungeon in dungeons_list]
        return dungeons

    def get_dungeon_link(self, dungeon_name):
        dungeons = self.dungeon_names()
        for dungeon in dungeons:
            if dungeon[0] == dungeon_name:
                return dungeon[1]

    def get_dungeon_page(self, dungeon_name):
        dungeon_redirect = self.get_dungeon_link(dungeon_name)
        return PuzzlesDragons.read_dungeon_page_soup(dungeon_redirect)

    def get_dungeon_content(self, dungeon_name):
        dungeon_page = self.get_dungeon_page(dungeon_name)
        content = dungeon_page.find(id="content")        
        return content