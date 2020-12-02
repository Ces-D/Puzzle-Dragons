from Content.contents import MonsterContent


class Profile(MonsterContent):
    def __init__(self, page):
        MonsterContent.__init__(self, page)

    def name(self):
        names = self.content_profile()[0].find_all(class_="data")
        return names[0].get_text()

    def measurements(self):
        measurements = self.content_profile()[1].find_all(class_="data")
        return measurements

    def type_(self):
        measurements = self.measurements()
        type_ = measurements[0].get_text()
        return type_

    def element(self):
        measurements = self.measurements()
        element = measurements[1].get_text()
        return element

    def rarity(self):
        measurements = self.measurements()
        rarity = measurements[2].get_text()
        return rarity

    def cost(self):
        measurements = self.measurements()
        cost = measurements[3].get_text()
        return cost

    def monster_points(self):
        measurements = self.measurements()
        monster_points = measurements[4].get_text()
        return monster_points

    def limit_break(self):
        measurements = self.measurements()
        limit_break = measurements[5].get_text()
        # format response
        return limit_break.split("\r\n\t\t\t\t\t\t\t\t\t\t\t")[1]
