from Profiles.monster_profile import Profile
from Skills.monster_skills import AwokenSkills, Skills
from pad import MonsterContent, PuzzlesDragons


class MonsterStats:

    @staticmethod
    def monster_profile(monster_id):
        monster_page = PuzzlesDragons.read_monster_soup(monster_id=monster_id)
        profile = Profile(page=monster_page)
        skills = Skills(page=monster_page)
        awoken_skills = AwokenSkills(page=monster_page)
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
                    "awakenings": awoken_skills.awoken_skills(),
                    "super_awakenings": awoken_skills.monster_super_awakenings_links()
                }
            ]
        }
        return monster_profile
