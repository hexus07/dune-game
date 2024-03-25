from dataclasses import dataclass

@dataclass
class PlayerAttributes:
    def __init__(self):
        self.attribs = {}

    def return_attributes(self):
        return self.attribs

    def add_attributes(self, attributes):
        self.attribs.update(attributes)
    def change_attributes(self, attribute, value):
        self.attribs[attribute] += value