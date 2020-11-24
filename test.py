# TODO: Get base url
# TODO: add number id to end of url
# TODO: request the page
# TODO: read the page
# TODO: find the tags for the appropriate information
# TODO: Create system to store the values of the monsters (update on run or one time only)
# TODO: Do the same for the dungeons
# TODO: Create way to search the dungeon opponents and map the counter abilities to the appropriate monster


from monsters import MonsterStats
from pad import PuzzlesDragons, UpdatedMonstersContent
from Player.monster_box import MonsterBox

# monster_profile = MonsterStats.monster_profile(monster_id="6596")

# print(monster_profile)

# # updated_c = UpdatedMonstersContent(PuzzlesDragons.read_home_page_soup())
# # print(updated_c.updated_monster_links())


MonsterBox.create_monster_box()