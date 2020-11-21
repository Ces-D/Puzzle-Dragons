# TODO: Get base url
# TODO: add number id to end of url
# TODO: request the page
# TODO: read the page
# TODO: find the tags for the appropriate information
# TODO: Create system to store the values of the monsters (update on run or one time only)
# TODO: Do the same for the dungeons
# TODO: Create way to search the dungeon opponents and map the counter abilities to the appropriate monster


from pad import PuzzlesDragons, MonsterStats, Profile

pd = PuzzlesDragons()

monster_page = pd.read_monster_soup(pd.request_monster_page("5078"))

ms = MonsterStats(monster_page=monster_page)

monster_profile = ms.monster_profile()

print(monster_profile)
