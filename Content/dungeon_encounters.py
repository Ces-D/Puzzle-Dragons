from os import stat


class Enemy:

    @staticmethod
    def floor(enemy_div):
        return enemy_div.get_text()

    @staticmethod
    def name(enemy_div):
        return enemy_div.img.get("title")

    @staticmethod
    def type_(enemy_div):
        return [e.get("title") for e in enemy_div.select("img")]

    @staticmethod
    def turn(enemy_div):
        return enemy_div.get_text()

    @staticmethod
    def attack(enemy_div):
        return enemy_div.get_text()

    @staticmethod
    def defence(enemy_div):
        return enemy_div.get_text()

    @staticmethod
    def health_points(enemy_div):
        return enemy_div.get_text()

    @staticmethod
    def memo(enemy_div):
        # seperating names and text
        element_names = enemy_div.find_all("a")
        names = [name.get_text()
                 for name in element_names if name.get_text() != ".."]
        # remove \xa0\xa0 and â\x89¥

        # split by the names and then match the names to the details
        if names !=[""]:
            element_text = enemy_div.find_all(text=True)
            uncleaned_details = "".join(element_text)
            cleaned_details = uncleaned_details.replace(
                "\xa0\xa0", "").replace("â\x89¥", "").replace("ã\x80\x80", "").replace("ï¼¯", "'O',").replace("\x8dï¼", "-,").split("..")
            details = []
            for i in range(len(cleaned_details)):
                try:
                    details.append(
                        (names[i], cleaned_details[i].split(names[i], 1)[1]))
                except IndexError:
                    details.append(("Additional", cleaned_details[i]))
            return details
        return names


class DungeonEncounters:
    def __init__(self, page):
        self.dungeon_page = page

    def dungeon_info(self):
        return self.dungeon_page.find(id="dungeon-info")

    def get_enemy_rows(self):
        """Find the table rows containing the dungeon enemies  

        Returns:
            [List]: list of dungeon enemies including the pages <tr> styling rows
        """
        dungeon_info = self.dungeon_info()
        enemy_rows = [table_row for table_row in dungeon_info.select(
            "table#tabledrop tr")[5:-2]]
        return enemy_rows

    def enemies(self):
        """ From enemy info list get just the enemies info

        Returns:
            [List]: list of just dungeon enemies
        """
        enemy_rows = self.get_enemy_rows()
        enemies = []
        # if row is a styling element skip else add info to list
        for enemy in enemy_rows:
            if enemy.find(class_="floorheader") or enemy.find(class_="floorcontainer"):
                continue
            else:
                enemies.append(enemy)
        return enemies

    def enemies_info(self):
        enemies = self.enemies()
        enemies_info = []
        for enemy in enemies:
            enemy_div = enemy.select("td")
            response = {
                "floor": Enemy.floor(enemy_div[0]),
                "enemy": Enemy.name(enemy_div[1]),
                "type_": Enemy.type_(enemy_div[2]),
                "turn": Enemy.turn(enemy_div[3]),
                "attack": Enemy.attack(enemy_div[4]),
                "defence": Enemy.defence(enemy_div[5]),
                "hp": Enemy.health_points(enemy_div[6]),
                "memo": Enemy.memo(enemy_div[7])}
            enemies_info.append(response)
        return enemies_info
