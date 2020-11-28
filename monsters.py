from Profiles.monster_profile import Profile
from Skills.monster_skills import Skills
from pad import PuzzlesDragons


class MonsterStats:

    @staticmethod
    def monster_profile(monster_id, res_type="dict_"):
        monster_page = PuzzlesDragons.read_monster_soup(monster_id=monster_id)
        profile = Profile(page=monster_page)
        skills = Skills(page=monster_page)
        if res_type == "tuple_":
            monster_profile = (
                monster_id, profile.name(),
                profile.type_(), profile.element(),
                profile.rarity(), profile.cost(),
                profile.monster_points(),
                profile.limit_break(), skills.active_skill_name(),
                skills.active_skill_effect(),
                skills.active_skill_cooldown(),
                skills.assist_status(),
                skills.leader_skill_name(),
                skills.leader_skill_effect(),
                ". ".join(skills.awoken_skills()),
                ". ".join(skills.super_awoken_skills())
            )
        else:
            monster_profile = {
                "monster_id": monster_id,
                "name": profile.name(),
                "type_": profile.type_(),
                "element": profile.element(),
                "rarity": profile.rarity(),
                "cost": profile.cost(),
                "monster_points": profile.monster_points(),
                "limit_break": profile.limit_break(),
                "active_skill": skills.active_skill_name(),
                "active_skill_effect": skills.active_skill_effect(),
                "active_skill_cooldown": skills.active_skill_cooldown(),
                "assist_status": skills.assist_status(),
                "leader_skill": skills.leader_skill_name(),
                "leader_skill_effect": skills.leader_skill_effect(),
                "awakenings": ". ".join(skills.awoken_skills()),
                "super_awakenings": ". ".join(skills.super_awoken_skills())
            }
        return monster_profile
