# TODO: Get base url
# TODO: add number id to end of url
# TODO: request the page
# TODO: read the page
# TODO: find the tags for the appropriate information
# TODO: Create system to store the values of the monsters (update on run or one time only)
# TODO: Do the same for the dungeons
# TODO: Create way to search the dungeon opponents and map the counter abilities to the appropriate monster


from monsters import MonsterStats
from pad import PuzzlesDragons, UpdatedMonstersContent, DungeonContent
from Player.monster_box import MonsterBox

# monster_profile = MonsterStats.monster_profile(monster_id="5236")
# print(monster_profile)
# updated_c = UpdatedMonstersContent(PuzzlesDragons.read_home_page_soup())
# print(updated_c.updated_monster_ids())

# MonsterBox.create_monster_box()
# MonsterBox.add("6129")
# MonsterBox.remove("5241")
# MonsterBox.check_for_updates()
# MonsterBox.list_monster_box()

d = DungeonContent(PuzzlesDragons.read_home_page_soup())
t1 = d.get_dungeon_tables()
print(t1)
