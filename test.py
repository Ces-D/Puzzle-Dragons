# TODO: Get base url
# TODO: add number id to end of url
# TODO: request the page
# TODO: read the page
# TODO: find the tags for the appropriate information
# TODO: Create system to store the values of the monsters (update on run or one time only)
# TODO: Do the same for the dungeons
# TODO: Create way to search the dungeon opponents and map the counter abilities to the appropriate monster


from monsters import MonsterStats
from pad import PuzzlesDragons
from Content.contents import DungeonContent
from Content.dungeon_encounters import DungeonEncounters, DungeonInfo
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

dungeon_c = DungeonContent(PuzzlesDragons.read_home_page_soup())
# t1 = d.dungeon_names() #{'Extreme Challenge Arena': 'redirect.asp?d=1012'}
# print(t1[0])
dungeon = dungeon_c.get_dungeon_content('Libertas Descended!')
# print(dungeon)

de = DungeonInfo(dungeon)
# info = de.dungeon_info()
# enemy_rows = de.get_enemy_rows() #5 is the first enemey
# enemies = de.enemies()
# print(enemies[0], "\n\n\n", enemies[-1])
# enemy_info = de.enemies_info()
# print(enemy_info)
print(de.sub_dungeon())

