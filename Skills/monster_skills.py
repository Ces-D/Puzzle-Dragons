import requests

class AwokenSkills:
    def __init__(self, contents):
        self.contents = contents

    def monster_awoken_abilities(self):
        """Both Awoken and Super Awoken abilities

        Returns:
            List: containing awoken and super awoken skills specific to a monster
        """
        skills = self.contents[3]
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

    def awoken_skills(self):
        awoken_skills=[]
        pass

    def super_awoken_skills(self):
        super_awoken_skills=[]
        pass


class Skills(AwokenSkills):
    def __init__(self, contents):
        AwokenSkills.__init__(self, contents)
        self.contents = contents

    def abilities(self):
        """ Unique class name for a monsters abilities

        Returns:
            List: A list of bs4 objects containing a monsters abilities
        """
        abilities = self.contents[3]
        return abilities.find_all(class_="value-end")

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
