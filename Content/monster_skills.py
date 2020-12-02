from Content.contents import AwokenSkillsContent, MonsterContent

class Skills(MonsterContent, AwokenSkillsContent):
    def __init__(self, page):
        MonsterContent.__init__(self, page)
        AwokenSkillsContent.__init__(self, page)

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
        links_list = self.monster_awakenings_links()
        return [AwokenSkillsContent.awakening_description(link) for link in links_list]

    def super_awoken_skills(self):
        links_list = self.monster_super_awakenings_links()
        return [AwokenSkillsContent.awakening_description(link) for link in links_list]
