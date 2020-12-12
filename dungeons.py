from Content.dungeon_encounters import DungeonInfo
from Content.contents import DungeonContent
from pad import PuzzlesDragons


class DungeonStats:
    @staticmethod
    def dungeon_stats(dungeon_name):
        dungeon_c = DungeonContent(PuzzlesDragons.read_home_page_soup())
        dungeon_page = dungeon_c.get_dungeon_content(dungeon_name=dungeon_name)
        dungeon = DungeonInfo(dungeon_page=dungeon_page)
        sub_dungeon = dungeon.sub_dungeon()
        dungeon_info = {
            "dungeon_name": sub_dungeon[0],
            "stamina": sub_dungeon[1],
            "battles": sub_dungeon[2],
            "attention": dungeon.dungeon_attention(),
            "major_encounters": dungeon.dungeon_encounters(),
        }
        return dungeon_info
